from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


class UserModelAdmin(UserAdmin):
    ordering = ("-create_at",)
    list_display = ("id", "email", "is_superuser", "create_at")
    list_filter = ("is_superuser", "create_at")
    search_fields = ("id", "email")
    list_display_links = ("id", "email")
    # espacios del modelo que se pueden editar

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "role",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "role", "email", "password1", "password2"),
            },
        ),
    )


class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ("city", "phone", "user", "Car")
    list_filter = ("city",)
    # asi se hace para los foreing keys
    search_fields = ("user__name", "Car__number")


class ClientProfileAdmin(admin.ModelAdmin):
    list_display = (
        "city",
        "phone",
        "user",
    )
    list_filter = ("city",)
    # asi se hace para los foreing keys
    search_fields = (
        "user__name",
        "Car__number",
    )
