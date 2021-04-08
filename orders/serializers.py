from rest_framework import serializers
from products.serializers import ProductSerializer
from .models import Order


class OrderCheckSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    total_price = serializers.FloatField(read_only=True)
    status = serializers.CharField(max_length=64, read_only=True)
    description = serializers.CharField(max_length=720, read_only=True)
    product_list = serializers.ListField()
    client_id = serializers.IntegerField(read_only=True)


class ProductOrderSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    description = serializers.CharField()
    image = serializers.CharField()
    category = serializers.CharField()


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    total_price = serializers.FloatField(read_only=True)
    status = serializers.CharField(max_length=64, read_only=True)
    product_list = ProductOrderSerializer(many=True)
    client_id = serializers.IntegerField(read_only=True)
