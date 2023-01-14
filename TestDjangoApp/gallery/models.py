from django.db import models
from django.urls import reverse
from django.core.validators import validate_image_file_extension
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='/media')
class FavoriteImages(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(favorite=True)


# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=120, null=True)
    photo = models.ImageField(upload_to='media/')
    date_uploaded = models.DateTimeField(auto_now=True)
    favorite = models.BooleanField(default=False, blank=False)
    slug = models.SlugField(null=True, blank=True)

    gallery = models.Manager()
    gallery_favorites = FavoriteImages()

    def get_absolute_url(self):
        return reverse("gallery:view_image", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("gallery:delete_image", kwargs={"pk": self.pk})

    def mark_as_favorite(self):
        return reverse("gallery:favorite_image", kwargs={"pk": self.pk})


    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)
