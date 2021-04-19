from rest_framework import authentication, permissions
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import OrderSerializer
from .models import Order
from .mixins import OrdersMixin


class OrderView(GenericViewSet, OrdersMixin, ListModelMixin):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer

    def get_queryset(self):
        client_id = self.request.user.id

        inventories_list = Order.objects.filter(client_id=client_id)

        return inventories_list
