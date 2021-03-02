from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, authentication, permissions

from django.core.exceptions import ObjectDoesNotExist

from .models import Inventory
from .serializers import InventorySerializer


class InventoryView(APIView):
    def get(self, request, product_id=""):
        inventories_list = Inventory.objects.all()

        if product_id:
            try:
                product = Inventory.objects.get(product_id=product_id)
            except ObjectDoesNotExist:
                return Response({"message": "this product does not exist in inventory"}, status=status.HTTP_404_NOT_FOUND)

            serializer = InventorySerializer(product)

            return Response(serializer.data, status=status.HTTP_200_OK)

        if not inventories_list:
            return Response({"message": "there are no products in inventory"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InventorySerializer(inventories_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RefuelView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def put(self, request, product_id=""):
        amount = request.data.get("amount")

        try:
            inventory = Inventory.objects.get(id=product_id)
        except ObjectDoesNotExist:
            return Response({"message": "does not have products in the inventory"}, status=status.HTTP_404_NOT_FOUND)

        inventory.amount += amount
        inventory.transaction_type = 'refuel'
        inventory.available_product()
        inventory.save()

        serializer = InventorySerializer(inventory)

        return Response(serializer.data, status=status.HTTP_200_OK)
