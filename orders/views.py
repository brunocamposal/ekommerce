from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.utils import timezone
from django.contrib.auth.models import User

from .serializers import OrderSerializer, OrderCheckSerializer
from .models import Order
from .services.total_price import calculate_total_price

from products.models import Product
from inventories.models import Inventory, InventoryRecords


class OrderView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        serializer = OrderCheckSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        new_prods = []

        for id_product in request.data['product_list']:
            product = Product.objects.get(id=id_product)
            inventory = Inventory.objects.get(id=product.inventory_id)

            if inventory.total_amount > 0:
                inventory.total_amount -= 1
                inventory.save()

                new_prods.append(product)

                # registrar no estoque a venda
                seller = User.objects.get(id=request.user.id)
    
                InventoryRecords.objects.create(
                    amount=1, transaction_type="sale", transaction_time=timezone.now(), product=inventory.product, seller=seller)

            else:
                return Response({'message': f'{product.name} out of stock.'},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        order = Order.objects.create(
            total_price=calculate_total_price(new_prods),
            status="REALIZADO",
            client_id=request.user.id
        )

        order.product_list.set(new_prods)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request):

        if request.data['status'] == 'ENVIADO':
            order = Order.objects.get(id=request.data['id'])
            order.status = request.data['status']
            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.data['status'] == 'ENTREGUE':
            order = Order.objects.get(id=request.data['id'])
            order.status = request.data['status']
            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.data['status'] == 'CANCELADO':
            order = Order.objects.get(id=request.data['id'])
            order.status = request.data['status']

            product_list = order.product_list.all()

            for product in product_list:
                inventory = Inventory.objects.get(product_id=product.id)
                inventory.total_amount += 1
                inventory.save()

            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
