from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('food', views.ItemViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]