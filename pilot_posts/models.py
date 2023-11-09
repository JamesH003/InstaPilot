from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Airline(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    identifier = models.CharField(max_length=3, null=False, blank=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder', null=False, blank=False)
    caption = models.TextField(max_length=100, null=False, blank=False)
    airline = models.ForeignKey(Airline, on_delete=models.SET_NULL, null=True, blank=True)
    flight_number = models.CharField(max_length=10, null=False, blank=False)
    location = models.CharField(max_length=80)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def image_preview(self):
        from django.utils.html import format_html
        return format_html(f"<img src='{self.image.url}' height='150'>")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.flight_number