from .views import ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductView)


urlpatterns = router.urls