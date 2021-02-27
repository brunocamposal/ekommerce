from django.shortcuts import render
from rest_framework.view import APIView
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Order


class OrderView(APIView):

    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if not serializer.is_valid():
            Response(status=status.HTTP_404_NOT_FOUND)

        order = Order.objects.create(**request.data)

        total_products_price = 0
        for product in request.data['products_list']:
            product = Product.objects.get(id=product)

            if product.amount > 0:
                Product.objects.filter(id=product).update(
                    amount=product.amount - 1)

                total_products_price = total_products_price + product.price
                order.products_list.add(product)
            else:
                Response({'message': f'{product.name} out of stock.'},
                         status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        order.total_price = total_products_price
        order.client_id = request.user.id

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
