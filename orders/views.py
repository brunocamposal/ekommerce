from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import OrderSerializer, OrderCheckSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from products.models import Product
from inventories.models import Inventory
# import ipdb


class OrderView(APIView):

    def post(self, request):
        serializer = OrderCheckSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        total_products_price = 0
        new_prods = []

        order = Order.objects.create(
            total_price=request.data['total_price'],
            description=request.data['description'],
            status=request.data['status'],
            client_id=request.data['client_id']
        )

        for id_product in request.data['product_list']:
            product = Product.objects.get(id=id_product)
            inventory = Inventory.objects.get(id=product.inventory_id)

            if inventory.amount > 0:
                Inventory.objects.filter(id=product.inventory_id).update(
                    amount=inventory.amount - 1)

                total_products_price = total_products_price + product.price
                new_prods.append(product)
            else:
                return Response({'message': f'{product.name} out of stock.'},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        order.product_list.set(new_prods)
        order.total_price = total_products_price

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
