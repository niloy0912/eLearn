# Generated by Django 5.0.3 on 2024-05-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('student', 'Student'), ('teacher', 'Teacher')], max_length=20, null=True),
        ),
    ]
