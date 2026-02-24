from django.urls import path
from .views import delete_course_view, delete_student, get_students, create_student, patch_student, update_student


urlpatterns = [
    path('api/', get_students, name='getStudent'),
    path('create/', create_student, name='createApiView'),
    path('update/<int:pk>/', update_student, name='updateApiView'),
    path('delete/<int:pk>/', delete_student, name='deleteApiView'),
    path('patch/<int:pk>/', patch_student, name='patchApiView'),
    path('create_student/', create_student, name='createStudent'),
    path('get_students/', get_students, name='getStudents'),
    path('patch_student/<int:pk>/', patch_student, name='patchStudent'),
    path('delete_course/<int:pk>/', delete_course_view, name='deleteCourse'),
    

]