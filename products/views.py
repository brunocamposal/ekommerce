from rest_framework import authentication, permissions
from accounts.permissions import IsSalesman

from rest_framework.viewsets import GenericViewSet
from .mixins import RegisterMixin
from .models import Product
from .serializers import ProductSerializer
from shared.pagination import CustomLimitOffsetPagination


class ProductView(GenericViewSet, RegisterMixin):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser | IsSalesman]
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = CustomLimitOffsetPagination
    ordering = ['id']
