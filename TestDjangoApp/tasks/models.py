from django.db import models
from django.db.models import F
from django.urls import reverse
# from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
import datetime as dt


# Create your models here.
class TodayTaskManager(models.Manager):
    def get_queryset(self):
        today = dt.date.today()
        return super().get_queryset().filter(date_due=today)


class Task(models.Model):
    summary = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    progress = models.IntegerField()
    active = models.BooleanField(default=True)
    date_added = models.DateField(auto_now=True)
    date_due = models.DateField()
    time_due = models.CharField(max_length=10, null=True, blank=True)
    objects = models.Manager()
    today_objects = TodayTaskManager()

    def get_absolute_url(self):
        return reverse("tasks:view_task", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return reverse("tasks:edit_task", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("tasks:delete_task", kwargs={"pk":self.pk})

    def __str__(self):
        return self.summary


