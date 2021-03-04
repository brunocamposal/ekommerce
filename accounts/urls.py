from django.urls import path

from .views import Signup, Login

urlpatterns = [
    path('accounts/', Signup.as_view()),
    path('login/', Login.as_view())
]