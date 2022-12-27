from rest_framework import serializers

from api.models import (
    ApplicationRegister,
    ApplicationsTransport,
    DriverProfile,
    ClientProfile,
)


class ApplicationsTransportSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    create_at = serializers.DateTimeField(read_only=True)
    client_profile = serializers.PrimaryKeyRelatedField(
        queryset=ClientProfile.objects.all()
    )
    driver_profile = serializers.PrimaryKeyRelatedField(
        queryset=DriverProfile.objects.all()
    )

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
