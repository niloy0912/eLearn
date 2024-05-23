from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import CourseMaterial
from .forms import CourseMaterialForm
from courses.models import Course
from django.contrib.auth.mixins import LoginRequiredMixin

class CourseMaterialListView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        materials = CourseMaterial.objects.filter(course=course)
        return render(request, 'course_material/material_list.html', {'course': course, 'materials': materials})

class CourseMaterialCreateView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        form = CourseMaterialForm()
        return render(request, 'course_material/material_form.html', {'form': form, 'course': course})

    def post(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        form = CourseMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.course = course
            material.created_by = request.user
            material.save()
            return redirect('course_material:material_list', course_id=course_id)
        return render(request, 'course_material/material_form.html', {'form': form, 'course': course})

class CourseMaterialUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        material = get_object_or_404(CourseMaterial, pk=pk)
        form = CourseMaterialForm(instance=material)
        return render(request, 'course_material/material_form.html', {'form': form, 'material': material})

    def post(self, request, pk):
        material = get_object_or_404(CourseMaterial, pk=pk)
        form = CourseMaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('course_material:material_list', course_id=material.course.id)
        return render(request, 'course_material/material_form.html', {'form': form, 'material': material})

class CourseMaterialDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        material = get_object_or_404(CourseMaterial, pk=pk)
        return render(request, 'course_material/material_confirm_delete.html', {'material': material})

    def post(self, request, pk):
        material = get_object_or_404(CourseMaterial, pk=pk)
        course_id = material.course.id
        material.delete()
        return redirect('course_material:material_list', course_id=course_id)
