from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Inventory, InventoryRecords
from .serializers import InventoryRecordsSerializer


class RecordsMixin:
    @action(detail=True, methods=["PUT"])
    def refuel(self, request, pk):
        amount = request.data.get("amount")
        sellerId = request.user.id

        inventory = get_object_or_404(Inventory, id=pk, seller=sellerId)
        seller = get_object_or_404(User, id=sellerId)

        inventory.total_amount += amount
        inventory.available_product()
        inventory.save()

        register_inventory = InventoryRecords.objects.create(
            amount=amount, transaction_type="refuel", transaction_time=timezone.now(), product=inventory.product, seller=seller)

        serializer = InventoryRecordsSerializer(register_inventory)

        return Response(serializer.data, status=status.HTTP_200_OK)
