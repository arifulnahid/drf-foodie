from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('orders', views.OrderViewSet)
router.register('carts', views.CartViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('v1/', include(router.urls))
# ]