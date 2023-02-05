from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from api.models import (
    ApplicationsTransport,
    ApplicationRegister,
    DriverProfile,
    ClientProfile,
    Car,
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
    queryset = ApplicationsTransport.objects.all()
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
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer


class Cars(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
