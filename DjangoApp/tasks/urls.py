from django.contrib import admin
from django.urls import path
from .views import add_task_view, edit_task_view, view_task, delete_task, all_tasks_view, search_task

app_name = 'tasks'
urlpatterns = [
    path('all/', all_tasks_view, name='all_tasks'),
    path('add/', add_task_view, name='add_task'),
    path('edit/<int:pk>/', edit_task_view, name='edit_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('<int:pk>/', view_task, name='view_task'),
    path('search/', search_task.as_view(), name='search_task'),
    ]