from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet

from api.models import (
    ApplicationsTransport,
    ApplicationRegister,
    DriverProfile,
    ClientProfile,
    Car,
    User,
)
from api.serializers import (
    ApplicationsTransportSerializer,
    ApplicationsRegisterSerializer,
    DriverProfileSerializer,
    ClientProfileSerializer,
    CarSerializer,
)


# Create your views here.


@api_view()
def main_api(request):
    return JsonResponse({"status": "ok"})


"""
with class
get list of applications register or send aplication register
"""


class Register(ModelViewSet):
    queryset = ApplicationRegister.objects.all()
    serializer_class = ApplicationsRegisterSerializer


"""
with class
get list of applications transport or send aplication to transport
"""


class Trasnsport(ModelViewSet):
    def get_queryset(self):
        user = self.request.user

        if user.role == "client":
            client = ClientProfile.objects.all().get(user=user)
            return ApplicationsTransport.objects.all().filter(
                client_profile_id=client.id
            )
        else:
            driver = DriverProfile.objects.all().get(user=user)
            return ApplicationsTransport.objects.all().filter(
                driver_profile_id=driver.id
            )

    serializer_class = ApplicationsTransportSerializer


"""
with class
get list of driver profile
"""


class Drivers(ModelViewSet):
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer


"""
get client list
"""


class Clients(ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return ClientProfile.objects.all().filter(user=user)

    serializer_class = ClientProfileSerializer


"""
like this form we can change permissions for methods 
"""


class Cars(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    def get_queryset(self):
        user = self.request.user

        driver = DriverProfile.objects.all().get(user=user)
        return Car.objects.all().filter(id=driver.Car_id)

    serializer_class = CarSerializer
