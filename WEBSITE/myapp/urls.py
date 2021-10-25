from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="myapp"),
path('contact/',views.contact,name='contact'),
path('blog/<int:id>',views.blog,name='blog'),
path('index1',views.index1,name='index1')
]