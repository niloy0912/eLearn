from django.db import models
from django.conf import settings
from courses.models import Course

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')

    def __str__(self):
        return self.title

class Submission(models.Model):
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"

class Grade(models.Model):
    score = models.FloatField()
    feedback = models.TextField()
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='grades')

    def __str__(self):
        return f"{self.submission.assignment.title} - {self.submission.student.username} - {self.score}"

