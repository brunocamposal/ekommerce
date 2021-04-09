from rest_framework import authentication, permissions
from rest_framework.viewsets import GenericViewSet

from .serializers import OrderSerializer
from .models import Order
from .mixins import OrdersMixin


class OrderView(GenericViewSet, OrdersMixin):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
