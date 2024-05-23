# Generated by Django 5.0.3 on 2024-05-22 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_student_enrolled_courses_and_more'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='enrolled_courses',
        ),
        migrations.AddField(
            model_name='student',
            name='enrolled_courses',
            field=models.ManyToManyField(related_name='students', to='courses.course'),
        ),
    ]
