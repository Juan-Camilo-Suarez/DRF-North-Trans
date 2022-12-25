from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from api.models import ApplicationRegister, User

# Register your models here.
admin.site.register(ApplicationRegister)


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
                "fields": ("role", "email", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, UserModelAdmin)
