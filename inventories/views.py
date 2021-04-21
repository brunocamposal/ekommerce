from rest_framework import authentication, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from accounts.permissions import IsSalesman
from shared.pagination import CustomLimitOffsetPagination

from .models import Inventory, InventoryRecords
from .serializers import InventorySerializer, InventoryRecordsSerializer
from .mixins import RecordsMixin


class InventoryView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Inventory.objects.all().order_by('id')
    serializer_class = InventorySerializer
    pagination_class = CustomLimitOffsetPagination
    ordering = ['id']


class RecordsView(GenericViewSet, RecordsMixin, ListModelMixin,  RetrieveModelMixin):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = InventoryRecords.objects.all().order_by('id')
    serializer_class = InventoryRecordsSerializer
    pagination_class = CustomLimitOffsetPagination
    ordering = ['id']


class ReportsView(GenericViewSet, ListModelMixin):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser | IsSalesman]
    queryset = InventoryRecords.objects.all().order_by('id')
    serializer_class = InventoryRecordsSerializer
    pagination_class = CustomLimitOffsetPagination
    ordering = ['id']

    def get_queryset(self):
        seller_id = self.request.user.id

        inventories_list = InventoryRecords.objects.filter(
            seller=seller_id, transaction_type="sale")

        return inventories_list
