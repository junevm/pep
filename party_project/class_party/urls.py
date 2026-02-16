from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_student, name='student_create'),
    path('list/', views.student_list, name='student_list'),
    path('orm-prep/', views.orm_prep, name='orm_prep'),
    path('insert-students/', views.insert_students, name='insert_students'),
    path('get_create/',views.get_or_create,name='get_create'),
    path('update_create/',views.update_or_create,name='update_create'),
    path('delete/',views.delete_student,name='delete_student'),
]
