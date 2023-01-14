from .forms import NoteForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.
def all_notes_view(request, *args, **kwargs):
    queryset = Note.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "notes/all_notes.html", context)


def view_notes(request, pk, *args, **kwargs):
    note = get_object_or_404(Note, id=pk)
    context = {
        'object': note
    }
    return render(request, "notes/note.html", context)

def add_notes_view(request, *args, **kwargs):
    form = NoteForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("../all")
    return render(request, "form.html", context)


def edit_notes_view(request, pk, *args, **kwargs):
    note = get_object_or_404(Note, id=pk)
    form = NoteForm(request.POST or None, instance=note)
    context = {
        'form': form
    }
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('../../all')
    return render(request, "form.html", context)

def delete_notes(request, pk, *args, **kwargs):
    note = get_object_or_404(Note, id=pk)
    if request.method == "POST":
        Note.objects.get(id=pk).delete()
        return redirect('../../all')

class search_note(ListView):
    models = Note
    template_name = "notes/all_notes.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Note.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list
