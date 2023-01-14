from django.urls import path
from .views import all_contacts_view, add_contacts_view, edit_contacts_view, delete_contacts, view_contact, search_contact

app_name = 'contacts'
urlpatterns = [
    path('add/', add_contacts_view, name='add_contact'),
    path('all/', all_contacts_view, name='all_contacts'),
    path('edit/<int:pk>/', edit_contacts_view, name='edit_contact'),
    path('delete/<int:pk>/', delete_contacts, name='delete_contact'),
    path('<int:pk>/', view_contact, name='view_contact'),
    path('search/', search_contact.as_view(), name='search_contact')
]