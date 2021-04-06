from .views import InventoryView, RecordsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'inventories', InventoryView)
router.register(r'records', RecordsView)

urlpatterns = router.urls
