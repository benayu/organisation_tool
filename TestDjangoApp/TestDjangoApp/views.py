from django.shortcuts import render, redirect
import sys
import datetime as dt
sys.path.insert(0, '/')
from tasks.models import Task
from contacts.models import Person
from gallery.models import Photo
import calendar
from calendar import HTMLCalendar
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/accounts/login')
def homepage_view(request, *args, **kwargs):
    month = dt.date.today().month
    year = dt.date.today().year
    day = dt.date.today().day
    cal = HTMLCalendar()
    cal = cal.formatmonth(theyear=year, themonth=month)
    queryset_1 = Task.today_objects.all()
    queryset_2 = Person.favorite_people.all()
    queryset_3 = Photo.gallery_favorites.all()
    cal = cal.replace('border="0" cellpadding="0" cellspacing="0"', 'class="table table-bordered table-sm"')
    cal = cal.replace(f'">{day}<', f' table-active">{day}<')

    context = {
        'today': dt.date.today().strftime('%b %d %Y'),
        'contacts_num': len(queryset_2),
        'task_num': len(queryset_1),
        'objects_list_1': queryset_1,
        'objects_list_2': queryset_2,
        'objects_list_3': queryset_3,
        'cal': cal

    }

    return render(request, "home.html", context)

