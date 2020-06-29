from django.contrib import admin
from django.urls import path
from django.urls import path,include
from  . import views
urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('blogPost', views.blogPost, name='blogPost')
]
