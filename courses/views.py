from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
# from django.views.generic import DetailView
from .models import Course, Enrollment
from assignments.models import Submission
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.models import Student


@method_decorator(login_required, name='dispatch')
class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses/course_list.html', {'courses': courses})

@method_decorator(login_required, name='dispatch')
class CourseDetailView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        assignments = course.assignments.all()
        enrolled_students = course.enrollments.all()
        is_enrolled = enrolled_students.filter(student=request.user).exists()
        return render(request, 'courses/course_detail.html', {
            'course': course,
            'assignments': assignments,
            'enrolled_students': enrolled_students,
            'is_enrolled': is_enrolled
        })

# class CourseDetailView(DetailView):
#     model = Course
#     template_name = 'courses/course_detail.html'
#     context_object_name = 'course'

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
class EnrollCourseView(View):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        # Check if the user is the teacher of the course
        if course.teacher == request.user:
            # Redirect to the course detail page with an error message
            return render(request, 'courses/course_detail.html', {
                'course': course,
                'enrolled_students': course.enrollments.all(),
                'is_enrolled': False,
                'error_message': "Teachers cannot enroll in their own courses."
            })
        
        # Check if the user is already enrolled
        if not Enrollment.objects.filter(student=request.user, course=course).exists():
            Enrollment.objects.create(student=request.user, course=course)
        
        return redirect('courses:course_detail', pk=pk)


# @method_decorator(login_required, name='dispatch')
# class StudentCourseListView(View):
#     def get(self, request):
#         context = {}
#         if request.user.is_authenticated and request.user.is_student:
#             enrollments = Enrollment.objects.filter(student=request.user)
#             enrolled_course_details = self.get_course_details(enrollments)
#             context['enrolled_course_details'] = enrolled_course_details
#         return render(request, 'courses/student_course_list.html', context)

#     def get_course_details(self, enrollments):
#         course_details = []
#         for enrollment in enrollments:
#             course = enrollment.course
#             assignments = course.assignments.all()
#             submissions = Submission.objects.filter(assignment__in=assignments, student=enrollment.student)
#             total_score = 0
#             total_marks = 0
#             assignment_grades = []

#             for assignment in assignments:
#                 submission = submissions.filter(assignment=assignment).first()
#                 grade = submission.grade if submission and hasattr(submission, 'grade') else None
#                 assignment_grades.append((assignment, grade))
#                 if grade:
#                     total_score += grade.score
#                     total_marks += assignment.total_marks

#             percentage = (total_score / total_marks * 100) if total_marks else 0
#             course_details.append({
#                 'course': course,
#                 'assignment_grades': assignment_grades,
#                 'percentage': percentage
#             })
#         return course_details


@method_decorator(login_required, name='dispatch')
class StudentCourseListView(View):
    def get(self, request):
        context = {}
        if request.user.is_authenticated and request.user.is_student:
            enrollments = Enrollment.objects.filter(student=request.user)
            enrolled_course_details = self.get_course_details(enrollments)
            context['enrolled_course_details'] = enrolled_course_details
        return render(request, 'courses/student_course_list.html', context)

    def get_course_details(self, enrollments):
        course_details = []
        for enrollment in enrollments:
            course = enrollment.course
            assignments = course.assignments.all()
            submissions = Submission.objects.filter(assignment__in=assignments, student=enrollment.student)
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