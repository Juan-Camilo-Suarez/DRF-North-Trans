"""NortTrans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from api.views import (
    main_api,
    Register,
    Trasnsport,
    Clients,
    Cars,
    Drivers,
    login_view,
)

"""
add simple router
"""
router = SimpleRouter()
router.register("register", Register, "applications register list")
router.register("transport", Trasnsport, "transport ")
router.register("driver", Drivers, "driver")
router.register("client", Clients, "client")
router.register("car", Cars, "car")
urlpatterns = [
    path("", main_api, name="example"),
    path("login/", login_view, name="login"),
    *router.urls,
]
