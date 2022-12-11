from django.db import models


# Create your models here.
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

    class Meta:
        verbose_name = "Application Register"
        verbose_name_plural = "Applications Register"
