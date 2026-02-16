from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # render the example page that extends base.html
    return render(request,'home.html')

