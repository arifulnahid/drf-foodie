from django.shortcuts import redirect
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from . import serializers


# Create your views here.
class UserRegistrationView(APIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://localhost:5173/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({'user': user.id, 'token': token, 'username':user.username})
        
        return Response(serializer.errors)

@api_view(['GET'])
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return Response({'message': 'Activation successful'})
    else:
        return Response({'message': 'Activation failed'}, status=400)

class UserLoginView(APIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer =self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)   
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user': user.id, 'username':user.username})
            else:
                return Response({'error': 'Username or Password is worng'})
        return Response(serializer.errors)

class UserLogoutView(APIView):
    def get(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfuly Logedout'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e.__str__())}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



