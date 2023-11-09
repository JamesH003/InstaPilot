from django.urls import path
from . import views


urlpatterns = [
    path('', views.UploadList.as_view(), name='home'),
    path('upload_post', views.upload_post, name="upload_post"),
