from django.urls import path
from .views import all_gallery_view, image_view, image_delete, image_new, favorite_image, search_image

app_name = 'gallery'
urlpatterns = [
    path('all/', all_gallery_view, name='gallery'),
    path('add/', image_new, name='add_image'),
    path('delete/<int:pk>/', image_delete, name='delete_image'),
    path('favorite/<int:pk>/', favorite_image, name='favorite_image'),
    path('<int:pk>/', image_view, name='view_image'),
    path('search/', search_image.as_view(), name='search_image')
]