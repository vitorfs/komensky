from django.shortcuts import render
from komensky.courses.models import Course
from komensky.courses.forms import CourseForm

def courses(request):
    return render(request, 'courses/courses.html')

def new(request):
    form = CourseForm()
    return render(request, 'courses/new.html', {'form': form})

def new(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/')
    else:
        form = CourseForm()
    return render(request, 'courses/new.html', {'form': form})