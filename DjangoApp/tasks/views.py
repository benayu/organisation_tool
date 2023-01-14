from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.views.generic import ListView
from django.db.models import Q
from .forms import TaskForm
# from .accounts.models import User
# from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='/accounts/login')
def all_tasks_view(request, *args, **kwargs):
    queryset = Task.objects.order_by('date_due')
    context = {
        "len": len(queryset),
        "object_list": queryset
    }

    return render(request, "tasks/all_tasks.html", context)


# @login_required(login_url='/accounts/login')
def view_task(request, pk, *args, **kwargs):
    task = get_object_or_404(Task, id=pk)
    context = {

        'object': task
    }
    return render(request, "tasks/task.html", context)


# @login_required(login_url='/accounts/login')
def add_task_view(request, *args, **kwargs):
    form = TaskForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect("../all")

    return render(request, "form.html", context)


# @login_required(login_url='/accounts/login')
def edit_task_view(request, pk,  *args, **kwargs):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(request.POST or None, instance=task)
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect("../../all")

    return render(request, "form.html", context)


# class view_task(DetailView):
#     template_name = "task.html"
#     queryset = Task.objects.all()
#
#
# class all_tasks_view(ListView):
#     template_name = "all_tasks.html"
#     queryset = Task.objects.all() #tasks/task_list.html
#

# @login_required(login_url='./accounts/login')
def delete_task(request, pk, *args, **kwargs):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        Task.objects.get(id=pk).delete()
    return redirect('../../all')


class search_task(ListView):
    models = Task
    template_name = "tasks/all_tasks.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        filter_complete = self.request.GET.get("filter_complete")
        if filter_complete:
            object_list = Task.objects.filter(
                Q(summary__icontains=query) | Q(description__icontains=query)).exclude(progress__gte=100).order_by('date_due')
        else:
            object_list = Task.objects.filter(
                Q(summary__icontains=query) | Q(description__icontains=query)).order_by('date_due')
        return object_list
