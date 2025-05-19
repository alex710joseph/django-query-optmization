from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderListView, order_list_view

router = DefaultRouter()
router.register(r'orders', OrderListView, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
    path('orders-page/', order_list_view, name='order-list-html'),
]