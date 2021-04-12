from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from inventories.models import Inventory, InventoryRecords
from products.models import Product
from .models import Order
from .serializers import OrderSerializer
from .services.total_price import calculate_total_price


class OrdersMixin:
    @action(detail=False, methods=["POST"])
    def create_order(self, request):
        product_list = request.data['product_list']
        user_id = request.user.id
        user_comments = request.data.get("comments", "no comments")
        new_prods = []

        for product_id in product_list:
            product = get_object_or_404(Product, id=product_id)
            inventory = Inventory.objects.get(id=product.inventory_id)

            if inventory.total_amount > 0:
                inventory.total_amount -= 1
                inventory.save()

                new_prods.append(product)
                
                # registrar no estoque a venda
                seller = User.objects.get(id=user_id)

                InventoryRecords.objects.create(
                    amount=1, transaction_type="sale", transaction_time=timezone.now(), product=inventory.product, seller=seller)

            else:
                return Response({'message': f'{product.name} out of stock.'},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        order = Order.objects.create(
            total_price=calculate_total_price(new_prods),
            status="REALIZADO",
            client_id=user_id,
            comments=user_comments
        )

        order.product_list.set(new_prods)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["PATCH"])
    def update_order(self, request):
        status = request.data['status']
        order_id = request.data['id']

        if status == 'ENVIADO':
            order = get_object_or_404(Order, id=order_id)
            order.status = status
            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data)

        if status == 'ENTREGUE':
            order = get_object_or_404(Order, id=order_id)
            order.status = status
            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data)

        if status == 'CANCELADO':
            order = get_object_or_404(Order, id=order_id)
            order.status = status

            product_list = order.product_list.all()

            for product in product_list:
                inventory = Inventory.objects.get(product_id=product.id)
                inventory.total_amount += 1
                inventory.save()

            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data)
