from .views import OrderView
from django.urls import path

urlpatterns = [
    path('orders/', OrderView.as_view()),
]
