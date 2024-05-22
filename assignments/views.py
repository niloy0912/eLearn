from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Assignment, Submission, Grade
from .forms import AssignmentForm, SubmissionForm, GradeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AssignmentListView(View):
    def get(self, request):
        assignments = Assignment.objects.all()
        return render(request, 'assignments/assignment_list.html', {'assignments': assignments})

@method_decorator(login_required, name='dispatch')
class AssignmentDetailView(View):
    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        submissions = assignment.submissions.all()
        return render(request, 'assignments/assignment_detail.html', {'assignment': assignment, 'submissions': submissions})

@method_decorator(login_required, name='dispatch')
class AssignmentCreateView(View):
    def get(self, request):
        course_id = request.GET.get('course_id')
        form = AssignmentForm(initial={'course': course_id})
        return render(request, 'assignments/assignment_form.html', {'form': form})

    def post(self, request):
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:course_detail', pk=form.cleaned_data['course'].pk)
        return render(request, 'assignments/assignment_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class AssignmentUpdateView(View):
    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        form = AssignmentForm(instance=assignment)
        return render(request, 'assignments/assignment_form.html', {'form': form})

    def post(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignments:assignment_detail', pk=pk)
        return render(request, 'assignments/assignment_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class AssignmentDeleteView(View):
    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        return render(request, 'assignments/assignment_confirm_delete.html', {'assignment': assignment})

    def post(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        assignment.delete()
        return redirect('assignments:assignment_list')

@method_decorator(login_required, name='dispatch')
class SubmissionCreateView(View):
    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        form = SubmissionForm()
        return render(request, 'assignments/submission_form.html', {'form': form, 'assignment': assignment})

    def post(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = request.user
            submission.save()
            return redirect('assignments:assignment_detail', pk=pk)
        return render(request, 'assignments/submission_form.html', {'form': form, 'assignment': assignment})

@method_decorator(login_required, name='dispatch')
class GradeAssignmentView(View):
    def get(self, request, pk):
        submission = get_object_or_404(Submission, pk=pk)
        form = GradeForm()
        return render(request, 'assignments/grade_form.html', {'form': form, 'submission': submission})

    def post(self, request, pk):
        submission = get_object_or_404(Submission, pk=pk)
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.submission = submission
            grade.save()
            return redirect('assignments:assignment_detail', pk=submission.assignment.pk)
        return render(request, 'assignments/grade_form.html', {'form': form, 'submission': submission})
