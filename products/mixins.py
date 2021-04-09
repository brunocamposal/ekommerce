from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .services.register import register_product

class RegisterMixin:
    @action(detail=False, methods=["POST"])
    def register(self, request):
        product = register_product(request.data, request.user.id)

        if product is None:
            return Response(
                {'data': {
                    'message': 'It was not possible to create the product, try again',
                    'error_code': 400
                }
                }, 400)

        return Response(product, 201)