from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Grade
from assignments.models import Assignment
from core.models import Student

@method_decorator(login_required, name='dispatch')
class GradeAssignmentView(View):
    def get(self, request, assignment_id, student_id):
        assignment = get_object_or_404(Assignment, id=assignment_id)
        student = get_object_or_404(Student, id=student_id)
        grade = Grade.objects.filter(assignment=assignment, student=student).first()
        context = {
            'assignment': assignment,
            'student': student,
            'grade': grade
        }
        return render(request, 'grades/grade_assignment.html', context)

    def post(self, request, assignment_id, student_id):
        assignment = get_object_or_404(Assignment, id=assignment_id)
        student = get_object_or_404(Student, id=student_id)
        score = request.POST['score']
        feedback = request.POST.get('feedback', '')
        grade, created = Grade.objects.update_or_create(
            assignment=assignment,
            student=student,
            defaults={'score': score, 'feedback': feedback}
        )
        return redirect('assignments:assignment_detail', assignment_id=assignment.id)
