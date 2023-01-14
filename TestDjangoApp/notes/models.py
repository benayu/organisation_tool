from django.db import models
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# import datetime as dt


class FavoriteNotesManager(models.Manager):
    def get_query_set(self):
        return super().get_query_set().filter(favorite=True)


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=120, null=True)
    content = RichTextField()
    date_added = models.DateTimeField(auto_now=True)
    favorite = models.BooleanField(default=False)
    objects = models.Manager()
    favorite_objects = FavoriteNotesManager()

    def get_absolute_url(self):
        return reverse("notes:view_note", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("notes:edit_note", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("notes:delete_note", kwargs={"pk":self.pk})
