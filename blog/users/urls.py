from django.conf.urls import url, include
from . import views
from django.contrib import admin

from users import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
     
        ]
