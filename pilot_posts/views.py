from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Airline, Upload
from .forms import UploadForm


class UploadList(generic.ListView):
    model = Upload
    queryset = Upload.objects.filter().order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12


@login_required
def upload_post(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Post uploaded successfully!')
            return redirect('home')
        messages.error(request, 'An error occured, please try again')
    context = {
        'form': form
    }
    return render(request, 'upload_post.html', context)


@login_required
def upload_details(request, id):
    upload = get_object_or_404(Upload, id=id)
    context = {
        'upload': upload
    }

    return render(request, 'upload_details.html', context)


@login_required
def edit_upload(request, id):
    upload = get_object_or_404(Upload, id=id)
    if not request.user.is_superuser and upload.user != request.user:
        messages.error(request, 'Access denied! Please try again')
        return redirect('home')
    form = UploadForm(
        request.POST or None, request.FILES or None, instance=upload)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = upload.user
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('home')
        messages.error(request, 'An error has occured, please try again')
    context = {
        'form': form,
        'upload': upload,
    }

    return render(request, 'edit_upload.html', context)


@login_required
def delete_post(request, id):
    upload = get_object_or_404(Upload, id=id)
    if not request.user.is_superuser and upload.user != request.user:
        messages.error(request, 'Access denied! Please try again')
        return redirect('home')
    upload.delete()
    messages.success(request, 'Post deleted successfully!')
    return redirect('home')
