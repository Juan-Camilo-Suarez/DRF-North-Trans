from django.contrib import admin


class CarAdmin(admin.ModelAdmin):
    list_display = ("number", "model", "capacity")
    list_filter = ("model", "capacity")
    search_fields = ("number",)
