from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Student, Teacher

@receiver(post_save, sender=User)
def create_student_record(sender, instance, created, **kwargs):
    if instance.is_student and not Student.objects.filter(user=instance).exists():
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_teacher_record(sender, instance, created, **kwargs):
    if instance.is_teacher and not Teacher.objects.filter(user=instance).exists():
        Teacher.objects.create(user=instance)
