
from django.contrib import admin
from django.urls import include, path
from crm.views import home_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home_page/', home_page, name='home_page'),
]
