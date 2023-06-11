
from django.contrib import admin
from django.urls import include, path
from users.views import register, login_view, personal_data
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('personal_data/', personal_data, name='personal_data'),
]
