from .views import OrderView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders', OrderView)

urlpatterns = router.urls
