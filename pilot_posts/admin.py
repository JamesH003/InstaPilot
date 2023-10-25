from django.contrib import admin
from .models import Upload


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ("user", "flight_number", "location", "image_preview")
    readonly_fields = ("image_preview", )
