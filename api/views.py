from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

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


@api_view(["GET", "POST"])
def application_register_list(request):
    # add application register
    if request.method == "POST":
        serializer = ApplicationsRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    else:
        applications_register = ApplicationRegister.objects.all()
        serializer = ApplicationsRegisterSerializer(applications_register, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def application_transport_list(request):
    if request.method == "POST":
        serializer = ApplicationsTransportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    else:
        applications_transport = ApplicationsTransport.objects.all()
        serializer = ApplicationsTransportSerializer(applications_transport, many=True)
        return Response(serializer.data)


@api_view()
def application_transport(request, id):
    applications_transport = get_object_or_404(
        ApplicationsTransport.objects.all(), id=id
    )
    serializer = ApplicationsTransportSerializer(applications_transport)
    return Response(serializer.data)


@api_view()
def driver_list(request):
    driver_profile = DriverProfile.objects.all()
    serializer = DriverProfileSerializer(driver_profile, many=True)
    return Response(serializer.data)


@api_view()
def client_list(request):
    client_profile = ClientProfile.objects.all()
    serializer = ClientProfileSerializer(client_profile, many=True)
    return Response(serializer.data)


@api_view()
def profile_client(request, id):
    client = get_object_or_404(ClientProfile.objects.all(), id=id)
    serializer = ClientProfileSerializer(client)
    return Response(serializer.data)


@api_view()
def car_list(request):
    car = Car.objects.all()
    serializer = CarSerializer(car, many=True)
    return Response(serializer.data)
