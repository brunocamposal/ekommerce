from rest_framework import serializers
from django.contrib.auth.models import User


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'username',
            'password',
            'is_superuser',
            'is_staff'
        ]
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'is_superuser': {'required': True},
            'is_staff': {'required': True}
        }
