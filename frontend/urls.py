from . import views
from django.urls import path
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('/project_details', views.project_details, name='project_details'),
    path('/contact', views.contact, name='contact'),
]
