from django.contrib import admin
from .models import Airline, Upload


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ("name", "identifier")


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = (
        "user", "airline", "flight_number", "location", "image_preview")
    readonly_fields = ("image_preview", )
