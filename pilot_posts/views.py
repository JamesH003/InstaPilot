from django.shortcuts import render
from django.views import generic
from .models import Upload

class UploadList(generic.ListView):
    model = Upload
    queryset = Upload.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12