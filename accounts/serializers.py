from rest_framework import serializers


class AccountsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField()
    is_staff = serializers.BooleanField()
