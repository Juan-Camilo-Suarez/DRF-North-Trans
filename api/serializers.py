from rest_framework import serializers
from api.models import ApplicationRegister


class ApplicationsTransportSerializer(serializers.Serializer):
    pass


class ApplicationsRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationRegister
        fields = ("id", "name", "city", "email", "phone", "user_position")
