# Generated by Django 5.0.3 on 2024-05-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursematerial',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='course_materials/'),
        ),
        migrations.AlterField(
            model_name='coursematerial',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
