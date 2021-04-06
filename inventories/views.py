from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from accounts.permissions import IsSalesman

from .models import Inventory, InventoryRecords
from .serializers import InventorySerializer, InventoryRecordsSerializer
from .services import inventories_list_dict
from .pagination import CustomLimitOffsetPagination
from .mixins import RecordsMixin


class InventoryView(GenericViewSet, ListModelMixin):
    queryset = Inventory.objects.all().order_by('id')
    serializer_class = InventorySerializer
    pagination_class = CustomLimitOffsetPagination
    ordering = ['id']


class RecordsView(GenericViewSet, RecordsMixin, ListModelMixin,  RetrieveModelMixin):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser | IsSalesman]
    queryset = InventoryRecords.objects.all().order_by('id')
    serializer_class = InventoryRecordsSerializer
    pagination_class = CustomLimitOffsetPagination
    ordering = ['id']
