from django.urls import path
from .views import InventoryView, RefuelView, RecordsView

urlpatterns = [
    path("inventories/", InventoryView.as_view()),
    path("inventories/<int:product_id>/", InventoryView.as_view()),
    path("inventories/records/", RecordsView.as_view()),
    path("inventories/refuel/<int:product_id>/", RefuelView.as_view())
]
