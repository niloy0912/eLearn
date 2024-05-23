from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from courses.models import Course

# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
          
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')

    
    # enrolled_courses = models.ManyToManyField(Course, related_name='students', blank=True)
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Add related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Add related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
        
    def __str__(self):
        return self.username
    


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    enrolled_courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username




## Will be Shifted

# class Assignment(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     due_date = models.DateField()
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')

#     def __str__(self):
#         return self.title

# class Grade(models.Model):
#     score = models.FloatField()
#     feedback = models.TextField()
#     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')

#     def __str__(self):
#         return f'{self.assignment.title} - {self.student.user.username}'
