# First: activate the virtual environment
# virtualenv venv -p python3
# .\Scripts\activate
# On terminal:
# django-admin startproject (name of the project)

# On terminal:
# python manage.py runserver
# This is to start the app

# On terminal: python manage.py migrate
# Creates the necessary tables

# In settings.py

# INSTALLED_APPS = [
#     'django.contrib.admin', # Manage users as the admin
#     'django.contrib.auth', # Authorizes users
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]

# Create a new app using command
# python manage.py startapp [appname]

# After creating an app, create a model
# See models.py

# Add app into INSTALLED_APPS

# After creating a model
# python manage.py makemigrations
# python manage.py migrate


# On terminal:
# manage.py shell
#
# from products.models import Product
# Product.objects.all()
# Shows all the products

# Product.objects.create(title='Title', description='Lorem ipsum', price='1232')


# When changing models, delete migrations folder
