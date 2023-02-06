from django.contrib import admin

from api.admin.applications import ApplicationsTransportAdmin
from api.admin.car import CarAdmin
from api.admin.user import UserModelAdmin, DriverProfileAdmin, ClientProfileAdmin
from api.models import (
    ApplicationRegister,
    User,
    ClientProfile,
    Car,
    DriverProfile,
    ApplicationsTransport,
)

# Register your models here.
admin.site.register(ApplicationRegister)
admin.site.register(ClientProfile, ClientProfileAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(DriverProfile, DriverProfileAdmin)
admin.site.register(ApplicationsTransport, ApplicationsTransportAdmin)
admin.site.register(User, UserModelAdmin)
