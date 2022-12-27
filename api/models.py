from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models
from api.enums import ROLES, STATUS


# Create your models here.


class BaseModel(models.Model):
    # auto_now_add=True sirve para que se crea automatico cuando se cree un modelo
    create_at = models.DateTimeField(auto_now_add=True)
    # se actualiza con la fecha del momento de la actualizacion
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        # para que no se agrege este modelo a la base de datos
        abstract = True


class UserManager(DjangoUserManager):
    def create_user(self, username, password=None, **extra_fields):
        # en vez de username se usa email
        user = self.model(email=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        user = self.model(email=email, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save()
        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    # de esta manera se puede decir que atributo va hacer de username
    USERNAME_FIELD = "email"
    email = models.EmailField(unique=True, verbose_name="Email")
    name = models.CharField(max_length=255, verbose_name="Name", null=True)
    password = models.CharField(max_length=200, verbose_name="password")
    # regula quien puede ir al admin
    role = models.CharField(
        max_length=20, choices=ROLES, verbose_name="role", null=True
    )
    is_staff = models.BooleanField(default=False, verbose_name="is worker")

    def __str__(self):
        return self.name + " / " + self.role

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class ClientProfile(models.Model):
    city = models.CharField(max_length=120, blank=False, verbose_name="City")
    phone = models.CharField(max_length=120, blank=False, verbose_name="Phone")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="users_avatar/", null=True, blank=True)

    def __str__(self):
        return self.user.name + " / " + self.user.role

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Car(models.Model):
    number = models.CharField(max_length=120, blank=False, verbose_name="number")
    model = models.CharField(max_length=120, blank=False, verbose_name="model")
    capacity = models.IntegerField(verbose_name="capacity on kg")
    photo = models.ImageField(upload_to="cars/", null=True, blank=True)

    def __str__(self):
        return self.number + " -" + self.model

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class DriverProfile(models.Model):
    city = models.CharField(max_length=120, blank=False, verbose_name="City")
    phone = models.CharField(max_length=120, blank=False, verbose_name="Phone")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    Car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Car")

    def __str__(self):
        return self.user.name + " / " + self.user.role

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class ApplicationsTransport(models.Model):
    client_profile = models.ForeignKey(
        ClientProfile, on_delete=models.CASCADE, verbose_name="client"
    )
    driver_profile = models.ForeignKey(
        DriverProfile, on_delete=models.CASCADE, verbose_name="driver"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        verbose_name="Status",
        null=True,
        default="processing",
    )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="date created")
    commentary = models.TextField(null=True)
    photo = models.ImageField(upload_to="applications/", null=True, blank=True)
    invoice = models.ImageField(upload_to="applications/invoice", null=True, blank=True)

    def __str__(self):
        return (
            "Client "
            + self.client_profile.user.name
            + " Driver: "
            + self.driver_profile.user.name
        )

    class Meta:
        verbose_name = "Application For Transport"
        verbose_name_plural = "Applications For Transport"


class ApplicationRegister(models.Model):
    class TypeUser(models.TextChoices):
        client = "client", "client"
        driver = "driver", "driver"

    name = models.CharField(max_length=120, blank=False, verbose_name="Name")
    city = models.CharField(max_length=120, blank=False, verbose_name="City")
    email = models.EmailField(max_length=120, blank=False, verbose_name="Email")
    phone = models.CharField(max_length=120, blank=False, verbose_name="Phone")
    user_position = models.CharField(
        max_length=15,
        choices=TypeUser.choices,
        verbose_name="Type User",
    )

    def __str__(self):
        return self.name + " / " + self.city

    class Meta:
        verbose_name = "Application Register"
        verbose_name_plural = "Applications Register"
