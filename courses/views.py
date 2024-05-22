from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course, Enrollment
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses/course_list.html', {'courses': courses})

@method_decorator(login_required, name='dispatch')
class CourseDetailView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        enrolled_students = course.enrollments.all()
        is_enrolled = enrolled_students.filter(student=request.user).exists()
        return render(request, 'courses/course_detail.html', {
            'course': course,
            'enrolled_students': enrolled_students,
            'is_enrolled': is_enrolled
        })

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        if not Enrollment.objects.filter(student=request.user, course=course).exists():
            Enrollment.objects.create(student=request.user, course=course)
        return redirect('courses:course_detail', pk=pk)


@method_decorator(login_required, name='dispatch')
class CourseCreateView(View):
    def get(self, request):
        form = CourseForm()
        return render(request, 'courses/course_form.html', {'form': form})

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('courses:course_list')
        return render(request, 'courses/course_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class CourseUpdateView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(instance=course)
        return render(request, 'courses/course_form.html', {'form': form})

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses:course_detail', pk=course.pk)
        return render(request, 'courses/course_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class CourseDeleteView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        return render(request, 'courses/course_confirm_delete.html', {'course': course})

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return redirect('courses:course_list')

@method_decorator(login_required, name='dispatch')
class EnrollInCourseView(View):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        if not Enrollment.objects.filter(student=request.user, course=course).exists():
            Enrollment.objects.create(student=request.user, course=course)
        return redirect('courses:course_detail', pk=pk)

