from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name="myapp"),
path('contact/',views.contact,name='contact'),
path('blog/<int:id>',views.blog,name='blog'),
path('index1',views.index1,name='index1'),
#path('<str:slug>', views.blogPost, name="blogPost"),
path('signup', views.signup, name="signup"),
path('login', views.handleLogin, name="handleLogin"),
path('logout', views.handleLogout, name="handleLogout")
]