# serializers.py
from rest_framework import serializers
from ecommerce.models.order import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'total_price', 'is_successful']
