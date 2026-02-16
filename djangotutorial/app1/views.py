from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def reportcard(request):
    context = {
        'student_name': 'Rishabh Kumar',
        'student_roll': 101,
        'class_name': '12th Grade',
        'is_passed': True,
        'total_marks': 425,
        'percentage': 85.0,
        
        # List of subjects with marks
        'subjects': [
            {'name': 'Mathematics', 'marks': 95, 'total': 100},
            {'name': 'Physics', 'marks': 88, 'total': 100},
            {'name': 'Chemistry', 'marks': 82, 'total': 100},
            {'name': 'English', 'marks': 78, 'total': 100},
            {'name': 'Computer Science', 'marks': 92, 'total': 100},
        ],
        
        # List of hobbies
        'hobbies': ['Reading', 'Coding', 'Cricket', 'Photography']
    }
    return render(request, 'app1/reportcard.html',context)
