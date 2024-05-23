from django.db import models
from assignments.models import Assignment
from core.models import Student

# Create your models here.


class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    score = models.FloatField()
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.assignment.title} - {self.student.user.username}'
