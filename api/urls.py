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

from api.views import (
    main_api,
    application_transport_list,
    application_transport,
    driver_list,
    client_list,
    car_list,
    profile_client,
    ApplicationListViewRegister,
)

urlpatterns = [
    path("", main_api, name="example"),
    path(
        "applications_register/",
        ApplicationListViewRegister.as_view({"get": "list", "post": "create"}),
        name="applications register list",
    ),
    path(
        "applications_transport/",
        application_transport_list,
        name="applications for transport list",
    ),
    path(
        "application_transport/<int:id>/",
        application_transport,
        name="applications for transport list",
    ),
    path(
        "driver_list/",
        driver_list,
        name="driver list",
    ),
    path(
        "client_list/",
        client_list,
        name="client list",
    ),
    path(
        "car_list/",
        car_list,
        name="car list",
    ),
    path(
        "profile_client/<int:id>/",
        profile_client,
        name="profile client",
    ),
]
