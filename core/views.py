from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout
from .models import Student, Teacher
from django.views import View
from courses.models import Course
from assignments.models import Submission
from .forms import *


@method_decorator(login_required, name='dispatch')
class Home(View):
    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            context['username'] = request.user.username
            if request.user.is_student:
                self.ensure_student_record(request.user)
                student = get_object_or_404(Student, user=request.user)
                enrolled_courses = student.enrolled_courses.all()
                available_courses = Course.objects.exclude(students=student)

                enrolled_course_details = self.get_course_details(enrolled_courses, request.user)
                
                context['enrolled_course_details'] = enrolled_course_details
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
    
    def get_course_details(self, courses, user):
        course_details = []
        for course in courses:
            assignments = course.assignments.all()
            submissions = Submission.objects.filter(assignment__in=assignments, student=user)
            total_score = 0
            total_marks = 0
            assignment_grades = []

            for assignment in assignments:
                submission = submissions.filter(assignment=assignment).first()
                grade = submission.grade if submission and hasattr(submission, 'grade') else None
                assignment_grades.append((assignment, grade))
                if grade:
                    total_score += grade.score
                    total_marks += assignment.total_marks

            percentage = (total_score / total_marks * 100) if total_marks else 0
            course_details.append({
                'course': course,
                'assignment_grades': assignment_grades,
                'percentage': percentage
            })
        return course_details


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
                
                # print(user.password2)
                login(request, user)
                return redirect('home')  # Redirect to home page
            except IntegrityError:
                form.add_error('username', 'A user with that username already exists.')
        return render(request, 'registration/signup.html', {'form': form})


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('home')



# class LogIn(View):
#     def get(self, request):
        
#         print("login get called")
        
#         form = CustomAuthenticationForm()
#         # print(form.is_bound)
#         return render(request, 'registration/signup.html', {'form': form})

#     def post(self, request):
#         form = CustomAuthenticationForm(data=request.POST)
        
#         print("login post called")

#         # print(form.is_valid()) 
#         if form.is_valid():
#             print("form is valid")
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print(username, password)
#             user = authenticate(request, username=username, password=password)
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         # print(form.errors)
        
#         return render(request, 'registration/signup.html', {'form': form})  
    
            
# def logout_1(request):
    # print("Logout called")
    # logout(request)
    # return redirect('home')