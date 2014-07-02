from django.shortcuts import render, redirect, get_object_or_404
from komensky.courses.models import Course, Module
from komensky.courses.forms import CourseForm, ModuleForm

def courses(request):
    return render(request, 'courses/courses.html')

def new_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=Course(user=request.user))
        if form.is_valid():
            course = form.save()
            return redirect('/cursos/%d/' % course.pk)
    else:
        form = CourseForm()
    return render(request, 'courses/new_course.html', {'form': form})

def course(request, id):
    course = get_object_or_404(Course, pk=id)
    return render(request, 'courses/course_wizard.html', {'course': course})

def new_module(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=Module(course=course))
        if form.is_valid():
            module = form.save()
            return redirect('/cursos/%d/' % course.pk)
    else:
        form = ModuleForm()
    return render(request, 'courses/new_module.html', {'course': course, 'form': form, })