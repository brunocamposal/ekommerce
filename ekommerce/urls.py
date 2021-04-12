from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('inventories.urls')),
    path('api/', include('products.urls')),
    path('api/', include('orders.urls'))
]

