from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    marks = models.IntegerField()

# Steps for CRUD API in django-rest-framework (Library on top of django)
# Create virtual env
# python -m venv venv
# source venv/bin/activate
# pip install django
# pip install restframework
# django-admin startproject <project-name>
# django-admin startapp <app-name>
# Add the app to INSTALLED_APPS in settings.py, rest_framework and <your-app-name>
# Create model class
# python manage.py makemigrations to create miration files
# python manage.py migrate to apply those migrations (performs changes on the table)
# define views fns
# add them to urls
# python manage.py runserver to run/ restart server
# Test on Postman

# Lookup serializers, class based views https://www.django-rest-framework.org/
