from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework import mixins
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

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
    LoginSerializer,
    LoginResponseSerializer,
)


# Create your views here.


@api_view()
@permission_classes([])
def main_api(request):
    return JsonResponse({"status": "ok"})


@api_view(["POST"])
@permission_classes([])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid()

    email = serializer.validated_data["email"]
    password = serializer.validated_data["password"]
    user = authenticate(request, email=email, password=password)
    token_model, created = Token.objects.get_or_create(user=user)
    if user is None:
        raise AuthenticationFailed

    response_serializer = LoginResponseSerializer(
        {"token": token_model.key, "user": user}
    )
    return Response(response_serializer.data)


"""
with class
get list of applications register or send aplication register
"""


@permission_classes([])
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
