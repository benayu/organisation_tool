from django.db import models
from django.urls import reverse


class FavoritePersonManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(favorite=True)


# Create your models here.
class Person(models.Model):
    title = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    department = models.CharField(null=True, max_length=100, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    date_added = models.DateField(auto_now=True)
    favorite = models.BooleanField(default=False)
    objects = models.Manager()
    favorite_people = FavoritePersonManager()
    # picture = models.ImageField(null=True, blank=True)
    # requires the pillow library
    
    def get_absolute_url(self):
        return reverse("contacts:view_contact", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("contacts:edit_contact", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("contacts:delete_contact", kwargs={"pk": self.pk})

    def __str__(self):
        return self.last_name
