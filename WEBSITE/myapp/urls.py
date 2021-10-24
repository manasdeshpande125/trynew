from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="myapp"),
path('contact/',views.contact,name='contact')
]