from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'teacher__username')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    search_fields = ('student__username', 'course__title')


# admin.site.register(Course)
# admin.site.register(Enrollment)