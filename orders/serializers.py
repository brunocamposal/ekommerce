from rest_framework import serializers
from products.serializers import ProductSerializer

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    total_price = serializers.FloatField()
    status = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=720)
    product_list = ProductSerializer(many=True)
    client_id = serializers.IntegerField()