from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.
def all_gallery_view(request, *args, **kwargs):
    queryset = Photo.gallery.all()
    context = {
        'object_list': queryset,
        'len': len(queryset)
    }
    return render(request, "gallery/all_photos.html", context)


def image_view(request, pk, *args, **kwargs):
    photo = get_object_or_404(Photo, id=pk)
    context = {
        'object': photo
    }
    return render(request, "gallery/view_image.html", context)


def image_new(request, *args, **kwargs):
    form = PhotoForm(data=request.POST, files=request.FILES)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('../../all')
    context = {
        'form': form
    }
    return render(request, "form.html", context)


def image_delete(request, pk, *args, **kwargs):
    if request.method == 'POST':
        photo = Photo.gallery.get(pk=pk)
        photo.delete()
    return redirect('../../all')


def favorite_image(request, pk, *args, **kwargs):
    if request.method == 'POST':
        photo = Photo.gallery.get(pk=pk)
        if photo.favorite == True:
            photo.favorite = False
            photo.save()
        else:
            photo.favorite = True
            photo.save()
    return redirect('../../all')


class search_image(ListView):
    models = Photo
    template_name = "gallery/all_photos.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Photo.gallery.filter(
            Q(name__icontains=query)
        )
        return object_list
