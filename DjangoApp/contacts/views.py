from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
import datetime as dt
from .forms import ContactForm
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.
def all_contacts_view(request, *args, **kwargs):
    queryset = Person.objects.all()
    context = {
        "len": len(queryset),
        "object_list": queryset,
        "today": dt.date.today()
    }
    return render(request, "contacts/all_contacts.html", context)


def view_contact(request, pk, *args, **kwargs):
    contact = get_object_or_404(Person, id=pk)
    context = {
        'object': contact
    }
    return render(request, "contacts/contact.html", context)


def add_contacts_view(request, *args, **kwargs):
    form = ContactForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect("../all")
    return render(request, "form.html", context)

def edit_contacts_view(request, pk, *args, **kwargs):
    contact = get_object_or_404(Person, id=pk)
    form = ContactForm(request.POST or None, instance=contact)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        redirect("../../all")
    return render(request, "form.html", context)


def delete_contacts(request, pk, *args, **kwargs):
    contact = get_object_or_404(Person, id=pk)
    if request.method == "POST":
        Person.objects.get(id=id).delete()
        return redirect('../../all')
    context = {
        "object": contact
    }
    return render(request, "contacts/delete_contact.html", context)


class search_contact(ListView):
    models = Person
    template_name = "contacts/all_contacts.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Person.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(description__icontains=query)
        )
        return object_list
