# Generated by Django 5.0.3 on 2024-05-22 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='total_marks',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='grade',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='submission',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='grade', to='assignments.submission'),
        ),
    ]
