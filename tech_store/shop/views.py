from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

class OrderListView(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def list(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
def order_list_view(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})