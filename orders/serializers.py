from products.serializers import ProductSerializer
from rest_framework import serializers
from .models import Order



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    product_list = ProductSerializer(many=True)
