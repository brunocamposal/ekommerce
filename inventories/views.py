from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from .models import Inventory, InventoryRecords
from .serializers import InventorySerializer, InventoryRecordsSerializer
from .services import product_dict, inventories_list_dict


class InventoryView(APIView):
    def get(self, request, product_id=""):
        inventories_list = Inventory.objects.all()

        if product_id:
            try:
                inventory_product = Inventory.objects.get(
                    product_id=product_id)
            except ObjectDoesNotExist:
                return Response({"message": "this product does not exist in inventory"}, status=status.HTTP_400_BAD_REQUEST)

            inventory_product.product_data = product_dict(
                inventory_product.product)
            serializer = InventorySerializer(inventory_product)

            return Response(serializer.data, status=status.HTTP_200_OK)

        if not inventories_list:
            return Response({"message": "there are no products in inventory"}, status=status.HTTP_404_NOT_FOUND)

        updated_inventories = inventories_list_dict(inventories_list)
        serializer = InventorySerializer(updated_inventories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RecordsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        records_list = InventoryRecords.objects.all()

        if not records_list:
            return Response({"message": "there are no records of products in inventory"}, status=status.HTTP_404_NOT_FOUND)

        updated_inventories = inventories_list_dict(records_list)

        serializer = InventoryRecordsSerializer(updated_inventories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RefuelView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, product_id=""):
        amount = request.data.get("amount")

        try:
            inventory = Inventory.objects.get(product=product_id)
        except ObjectDoesNotExist:
            return Response({"message": "does not have products in the inventory"}, status=status.HTTP_404_NOT_FOUND)

        inventory.total_amount += amount
        inventory.available_product()
        inventory.save()

        register_inventory = InventoryRecords.objects.create(
            amount=amount, transaction_type="refuel", transaction_time=timezone.now(), product=inventory.product)

        serializer = InventoryRecordsSerializer(register_inventory)

        return Response(serializer.data, status=status.HTTP_200_OK)
