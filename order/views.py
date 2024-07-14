from django.shortcuts import redirect
from rest_framework import viewsets, filters
from . import serializers
from . import models

# Create your views here.
class SpecificUserFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.query_params.get('user')
        if user:
            return queryset.filter(user=user)
        return queryset
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    filter_backends = [SpecificUserFilter]
    

class CartViewSet(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer
    filter_backends = [SpecificUserFilter]
    
