from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('create/', views.create_employee, name='employee_create'),
    path('list/', views.employee_list, name='employee_list'),
    path('get_cookies/', views.get_cookies, name='get_cookies'),
    path('set_cookies/', views.set_cookies, name='set_cookies'),
    path('delete_cookies/', views.delete_cookies, name='delete_cookies'),
]
