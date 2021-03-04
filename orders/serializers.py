from rest_framework import serializers
from products.serializers import ProductSerializer
from .models import Order


class OrderCheckSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    total_price = serializers.FloatField()
    status = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=720)
    product_list = serializers.ListField()
    client_id = serializers.IntegerField()


class ProductOrderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    description = serializers.CharField()


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    total_price = serializers.FloatField()
    status = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=720)
    product_list = ProductOrderSerializer(many=True)
    client_id = serializers.IntegerField()
