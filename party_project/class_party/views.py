from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Student

# Create your views here.
def create_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Student.objects.create(name=name, email=email, phone=phone)

        return redirect('student_list')  
    
    return render(request, 'student/create.html')

def student_list(request):
    student = Student.objects.all()
    return render(request, 'student/list.html', {'students': student})  

def update_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.save()

        return redirect('student_list')  
    
    return render(request, 'student/update.html', {'student': student})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_list')

def insert_students(request):
    # Student.objects.create(name='John Doe', email='john@example.com', phone='1234567890')
    # Student.objects.create(name='Jane Smith', email='jane@example.com', phone='0987654321')
    return HttpResponse("Students inserted successfully")

def orm_prep(request):
    # Create
    studen_values = Student.objects.values()
    get_student_by_age = Student.objects.filter()
    print(get_student_by_age.query)
    print(studen_values)
    
    return HttpResponse("ORM prep completed")

def get_or_create(request):
    student, created = Student.objects.get_or_create(name="dsad",email="random@f.com",phone="4")
    print(student,created)
    return HttpResponse('All studentsf')

def update_or_create(request):
    student, created = Student.objects.update_or_create(email="random@f.com",defaults={'name': "Updated Name", 'phone': "9876543210"})
    print(student, created)
    return HttpResponse('Update or create completed')

def delete_student(request):
    student = Student.objects.get(id=request.GET.get('id'))
    student.delete()
    print(f"Deleted student: {student.name}")

    students = Student.objects.all()
    number_of_students = students.delete()

    print(f"Deleted {number_of_students[0]} students with 'John' in their name")
    return HttpResponse('Student deleted successfully')