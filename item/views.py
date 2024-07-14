from django.shortcuts import redirect
from rest_framework import viewsets, filters
from . import serializers
from . import models

# Create your views here.
class ItemForCategory(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        category = request.query_params.get('category')
        if category:
            return queryset.filter(category=category)
        return queryset

class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    filter_backends = [ItemForCategory]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
