from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from products.services.register import register_product
# Create your views here.

class ProductView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request):

        product = register_product(request.data)

        if product is None:
            return Response(
            {'data': {
                'message': 'Não foi possível criar o produto, tente novamente', 
                'error_code': 400
                }
            }, 400)

        return Response(product, 201)

        