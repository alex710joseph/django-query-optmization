from rest_framework import serializers
from .models import Customer, Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email']

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    customer= CustomerSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_date', 'products']
