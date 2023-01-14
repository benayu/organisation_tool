from django.urls import path
from .views import all_notes_view, add_notes_view, edit_notes_view, delete_notes, view_notes, search_note

app_name = 'notes'
urlpatterns = [
    path('all/', all_notes_view, name='all_tasks'),
    path('add/', add_notes_view, name='add_task'),
    path('edit/<int:pk>/', edit_notes_view, name='edit_note'),
    path('delete/<int:pk>/', delete_notes, name='delete_note'),
    path('<int:pk>/', view_notes, name='view_note'),
    path('search/', search_note.as_view(), name='search_note')
]