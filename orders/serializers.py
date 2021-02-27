from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    total_price = serializers.FloatField()
    status = serializer.CharField()
    description = serializer.CarField()
    product_list = ProductSerializer(many=True)
    client_id = IntegerField()