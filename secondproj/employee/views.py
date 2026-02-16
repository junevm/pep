from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Employee

# Create your views here.
def create_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        salary = request.POST.get('salary')


        Employee.objects.create(name=name, email=email, position=position, salary=salary)

        return redirect('employee_list')  
    
    return render(request, 'employee/create.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list.html', {'employees': employees})  

def get_cookies(request):
    name = request.COOKIES.get('name')
    last_name = request.COOKIES.get('last_name')
    return HttpResponse(f"Name: {name}, Last Name: {last_name}")

def set_cookies(request):
    response = HttpResponse("Cookies set")
    response.set_cookie('name', 'John')
    response.set_cookie('last_name', 'Doe')
    return response

def delete_cookies(request):
    response = HttpResponse("Cookies deleted")
    response.delete_cookie('name')
    response.delete_cookie('last_name')
    return response