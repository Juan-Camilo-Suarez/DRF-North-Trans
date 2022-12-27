from rest_framework import serializers

from api.models import (
    ApplicationRegister,
    ApplicationsTransport,
    DriverProfile,
    ClientProfile,
    User,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email", "role")


class ClientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ClientProfile
        fields = ("city", "phone", "user", "user_id")


class DriverProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DriverProfile
        fields = ("city", "phone", "user", "user_id", "Car")


class ApplicationsTransportSerializer(serializers.ModelSerializer):
    # client = ClientProfileSerializer()
    # driver = DriverProfileSerializer()
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
