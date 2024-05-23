from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout
from .models import Student, Teacher
from django.views import View
from courses.models import Course
from .forms import CustomUserCreationForm


@method_decorator(login_required, name='dispatch')
class Home(View):
    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            context['username'] = request.user.username
            if request.user.is_student:
                self.ensure_student_record(request.user)
                available_courses = Course.objects.all()
                context['available_courses'] = available_courses

            elif request.user.is_teacher:
                available_courses = Course.objects.filter(teacher=request.user)
                context['available_courses'] = available_courses
        return render(request, 'core/home.html', context)
    
    def post(self, request):
        return render(request, 'core/home.html')
    
    def ensure_student_record(self, user):
        if user.is_student and not Student.objects.filter(user=user).exists():
            Student.objects.create(user=user)
    
    def ensure_teacher_record(self, user):
        if user.is_teacher and not Teacher.objects.filter(user=user).exists():
            Teacher.objects.create(user=user)


class Register(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.username = form.cleaned_data['username']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.set_password(form.cleaned_data['password1'])
                user_type = form.cleaned_data['user_type']
                if user_type == 'student':
                    user.is_student = True
                elif user_type == 'teacher':
                    user.is_teacher = True
                user.save()
                
                login(request, user)
                return redirect('home')  # Redirect to home page
            except IntegrityError:
                form.add_error('username', 'A user with that username already exists.')
        return render(request, 'registration/signup.html', {'form': form})


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('home')
