from django.urls import path
from . import views


urlpatterns = [
    path('', views.UploadList.as_view(), name='home'),
    path('upload_post', views.upload_post, name="upload_post"),
    path('edit/<int:id>', views.edit_upload, name='edit_upload'),
    path('details/<int:id>', views.upload_details, name='upload_details'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
]
