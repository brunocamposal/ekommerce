from rest_framework import serializers

from .models import Inventory, InventoryRecords


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'available',
            'total_amount',
            'product_data',
        ]


class InventoryRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryRecords
        fields = [
            'id',
            'amount',
            'transaction_type',
            'transaction_time',
            'product'
        ]
