# Generated by Django 5.0.3 on 2024-05-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_user_enrolled_courses_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
