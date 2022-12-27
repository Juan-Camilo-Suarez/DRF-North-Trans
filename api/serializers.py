from rest_framework import serializers

from api.models import ApplicationRegister, ApplicationsTransport


class ApplicationsTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationsTransport
        fields = (
            "client_profile",
            "driver_profile",
            "status",
            "create_at",
            "commentary",
            "photo",
            "invoice",
        )


class ApplicationsRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationRegister
        fields = ("id", "name", "city", "email", "phone", "user_position")
