from rest_framework import serializers

from .models import Inventory, InventoryRecords
from .services import product_dict


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'available',
            'total_amount',
            'seller',
            'product_data',
        ]

    def to_representation(self, inventory):
        inventory.product_data = product_dict(inventory.product)
        return super().to_representation(inventory)


class InventoryRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryRecords
        fields = [
            'id',
            'amount',
            'transaction_type',
            'transaction_time',
            'seller',
            'product_data'
        ]

    def to_representation(self, inventory):
        inventory.product_data = product_dict(inventory.product)

        return super().to_representation(inventory)
