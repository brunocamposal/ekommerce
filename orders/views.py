from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .serializers import OrderSerializer, OrderCheckSerializer
from .models import Order
from products.models import Product
from inventories.models import Inventory


class OrderView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

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

            if inventory.total_amount > 0:
                inventory.total_amount -= 1
                inventory.save()

                total_products_price = total_products_price + product.price
                new_prods.append(product)
            else:
                return Response({'message': f'{product.name} out of stock.'},
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        order.product_list.set(new_prods)
        order.total_price = total_products_price

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request):

        if request.data['status'] == 'REALIZADO':
            order = Order.objects.get(id=request.data['id'])
            order.status = request.data['status']
            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

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
                inventory.amount += 1
                inventory.save()

            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
