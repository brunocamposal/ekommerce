from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from products.services.register import register_product
from accounts.permissions import IsSalesman
# Create your views here.


class ProductView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser | IsSalesman]

    def post(self, request):

        product = register_product(request.data, request.user.id)

        if product is None:
            return Response(
                {'data': {
                    'message': 'It was not possible to create the product, try again',
                    'error_code': 400
                }
                }, 400)

        return Response(product, 201)
