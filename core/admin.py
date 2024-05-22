from django.contrib import admin
from .models import User, Course, Assignment, Grade

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_student', 'is_teacher')
    search_fields = ('username',)

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'teacher')
#     search_fields = ('name', 'teacher__username')

# @admin.register(Assignment)
# class AssignmentAdmin(admin.ModelAdmin):
#     list_display = ('title', 'course', 'due_date')
#     search_fields = ('title', 'course__name')

# @admin.register(Grade)
# class GradeAdmin(admin.ModelAdmin):
#     list_display = ('score', 'assignment', 'student')
#     search_fields = ('assignment__title', 'student__username')
