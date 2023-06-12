
from django.contrib import admin
from django.urls import include, path
from crm.views import home_page, clients_page, updates_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home_page/', home_page, name='home_page'),
    path('clients_page/', clients_page, name='clients_page'),
    path('updates_page/', updates_page, name='updates_page'),
]
