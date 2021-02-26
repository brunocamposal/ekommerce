from django.urls import path
from .views import InventoryView, RefuelView

urlpatterns = [
    path("inventories/<str:category>/", InventoryView.as_view()),
    path("inventories/refuel/<int:inventory_id>/", RefuelView.as_view())
]
