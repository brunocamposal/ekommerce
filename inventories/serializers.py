from rest_framework import serializers

from .models import Inventory, InventoryRecords


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


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
