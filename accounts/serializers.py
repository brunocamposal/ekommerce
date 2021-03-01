from rest_framework import serializers
from django.contrib.auth.models import User


class AccountsSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'is_superuser',
            'is_staff'
        ]
