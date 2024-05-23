from django import forms
from .models import CourseMaterial

class CourseMaterialForm(forms.ModelForm):
    class Meta:
        model = CourseMaterial
        fields = ['title', 'content', 'file']  # Add file field
