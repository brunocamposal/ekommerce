from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from .models import Inventory
from .serializers import InventorySerializer


class InventoryView(APIView):
    def get(self, request, category=""):
        if category:
            try:
                inventories_list = Inventory.objects.get(category=category)
            except ObjectDoesNotExist:
                return Response({"message": "does not have products in the inventory of this category"}, status=status.HTTP_404_NOT_FOUND)

            serializer = InventorySerializer(inventories_list, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        inventories_list = Inventory.objects.all()
        serializer = InventorySerializer(inventories_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RefuelView(APIView):
    def put(self, request, inventory_id=""):
        amount = request.data.get("amount")

        try:
            inventory = Inventory.objects.get(id=inventory_id)
        except ObjectDoesNotExist:
            return Response({"message": "does not have products in the inventory"}, status=status.HTTP_404_NOT_FOUND)

        inventory.amount += amount
        inventory.save()

        serializer = InventorySerializer(inventory)

        return Response(serializer.data, status=status.HTTP_200_OK)

