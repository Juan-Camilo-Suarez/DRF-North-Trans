from django.contrib import admin


class ApplicationsTransportAdmin(admin.ModelAdmin):
    list_display = (
        "client_profile",
        "driver_profile",
        "status",
        "create_at",
    )
    list_filter = ("client_profile__city",)
    # asi se hace para los foreing keys
    search_fields = ("client_profile__user__name",)
