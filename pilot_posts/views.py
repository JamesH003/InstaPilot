from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Airline, Upload
from .forms import UploadForm

class UploadList(generic.ListView):
    model = Upload
    queryset = Upload.objects.filter().order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12


# def get_uploads(request):
#     uploads = Upload.objects.all().order_by('-created_on')
#     template = 'index.html'
#     context = {
#         'upload_list': uploads,
#     }
#     return render(request, template, context)


def upload_post(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'upload_post.html', context)


def upload_details(request, id):
    upload = get_object_or_404(Upload, id=id)
    context = {
        'upload': upload
    }

    return render(request, 'upload_details.html', context)

