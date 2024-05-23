from django import forms
from .models import Assignment, Submission, Grade

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'total_marks']
        widgets = {
            'course': forms.HiddenInput()
        }


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['content']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['score', 'feedback']
        
