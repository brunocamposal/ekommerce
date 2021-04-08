from .views import InventoryView, RecordsView, ReportsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'inventories', InventoryView)
router.register(r'records', RecordsView)
router.register(r'reports', ReportsView)

urlpatterns = router.urls
