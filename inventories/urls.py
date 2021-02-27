from django.urls import path
from .views import InventoryView, RefuelView

urlpatterns = [
    path("inventories/", InventoryView.as_view()),
    path("inventories/refuel/<int:product_id>/", RefuelView.as_view())
]
