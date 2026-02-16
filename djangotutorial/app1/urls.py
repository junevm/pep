from django.urls import path
from . import views

urlpatterns = [
   
    path('reportcard/', views.reportcard, name='reportcard'),
]           
