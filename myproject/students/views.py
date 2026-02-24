from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Student,Course

from .serializers import StudentSerializer,CourseSerializer

# Create your views here.
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_student(request):
    student_data = request.data
    ser = StudentSerializer(data = student_data)
    if ser.is_valid():
        ser.save()
        print(f'{student_data} is created successfully')
        return Response(ser.data)
    else:
        print(f'Error: {ser.errors}')
        return Response(ser.errors)

@api_view(['PUT'])
def update_student(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

    student_data = request.data
    ser = StudentSerializer(student, data=student_data)
    if ser.is_valid():
        ser.save()
        print(f'{student_data} is updated successfully')
        return Response(ser.data)
    else:
        print(f'Error: {ser.errors}')
        return Response(ser.errors)

@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

    student.delete()
    print(f'Student with id {pk} is deleted successfully')
    return Response({'message': 'Student deleted successfully'})

@api_view(['PATCH'])
def patch_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

    student_data = request.data
    ser = StudentSerializer(student, data=student_data, partial=True)
    if ser.is_valid():
        ser.save()
        print(f'Student with id {pk} is patched successfully')
        return Response(ser.data)
    else:
        print(f'Error: {ser.errors}')
        return Response(ser.errors)
    
@api_view(['POST'])
def create_student(request):
    data = request.data
    student = Student.objects.create(name=data.get('name'),age=data.get('age'))
    courses = data.get('courses',[])
    course_set = Course.objects.filter(id__in=courses)
    student.courses.add(*course_set)
    return Response({"success":"Student added"})


@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def patch_student(request, pk):
    student = Student.objects.get(pk=pk)
    
    data = request.data
    if 'name' in data:
        student.name = data['name']
    if 'age' in data:
        student.age = data['age']
    if 'courses' in data:
        courses = data['courses']['id']
        course_set = Course.objects.filter(id__in=courses)
        student.courses.set(course_set)
    student.save()
    return Response({"success": "Student updated successfully"})


@api_view(['DELETE'])
def delete_course_view(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=404)
    
    course.delete()
    
    return Response({'message': 'Course deleted successfully'})
    