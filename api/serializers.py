from rest_framework import serializers
from rest_framework.fields import CharField


class ApplicationsTransportSerializer(serializers.Serializer):
    pass


class ApplicationsRegisterSerializer(serializers.Serializer):
    name = serializers.CharField()
    city = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    user_position = serializers.CharField()
