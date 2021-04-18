from rest_framework import authentication, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from accounts.permissions import IsSalesman
from shared.pagination import CustomLimitOffsetPagination

from .models import Inventory, InventoryRecords
from .serializers import InventorySerializer, InventoryRecordsSerializer
from .mixins import RecordsMixin


class InventoryView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Inventory.objects.all().order_by('id')
    serializer_class = InventorySerializer
    pagination_class = CustomLimitOffsetPagination
    ordering = ['id']

    @method_decorator(cache_page(60*10))
    @method_decorator(vary_on_headers('Authorization'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


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
