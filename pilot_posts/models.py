from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder', null=False, blank=False)
    caption = models.TextField(max_length=100, null=False, blank=False)
    flight_number = models.CharField(max_length=10, null=False, blank=False)
    location = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)

    def image_preview(self):
        from django.utils.html import format_html
        return format_html(f"<img src='{self.image.url}' height='150'>")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.flight_number