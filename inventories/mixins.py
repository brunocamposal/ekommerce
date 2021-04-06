from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Inventory, InventoryRecords
from .serializers import InventoryRecordsSerializer


class RecordsMixin:
    @action(detail=True, methods=["PUT"])
    def refuel(self, request, pk):
        amount = request.data.get("amount")
        inventory = get_object_or_404(Inventory, id=pk)

        inventory.total_amount += amount
        inventory.available_product()
        inventory.save()
        
        register_inventory = InventoryRecords.objects.create(
            amount=amount, transaction_type="refuel", transaction_time=timezone.now(), product=inventory.product)
        
        serializer = InventoryRecordsSerializer(register_inventory)

        return Response(serializer.data, status=status.HTTP_200_OK)


