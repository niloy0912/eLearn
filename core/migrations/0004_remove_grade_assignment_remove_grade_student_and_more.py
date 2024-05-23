# Generated by Django 5.0.3 on 2024-05-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_assignment_course_remove_coursematerial_course_and_more'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='student',
        ),
        migrations.AlterField(
            model_name='student',
            name='enrolled_courses',
            field=models.ManyToManyField(related_name='students', to='courses.course'),
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]