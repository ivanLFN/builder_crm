
from django.contrib import admin
from django.urls import include, path
from crm.views import home_page, clients_page, updates_page, create_new_client, create_new_order, table_orders_page, search_view, result_detail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home_page/', home_page, name='home_page'),
    path('clients_page/', clients_page, name='clients_page'),
    path('updates_page/', updates_page, name='updates_page'),
    path('create_new_client/', create_new_client, name='create_new_client'),
    path('create_new_order/', create_new_order, name='create_new_order'),
    path('table_orders_page/', table_orders_page, name='table_orders_page'),
    path('search/', search_view, name='search'),
    path('result/<int:result_id>/', result_detail, name='result_detail'),
]
