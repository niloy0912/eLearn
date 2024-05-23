from django.contrib import admin
from .models import CourseMaterial

@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'course__title', 'created_by__username')
