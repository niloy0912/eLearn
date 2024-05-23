from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CourseMaterial
from .forms import CourseMaterialForm
from courses.models import Course

class CourseMaterialListView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        materials = course.materials.all()
        return render(request, 'course_material/material_list.html', {'course': course, 'materials': materials})

class CourseMaterialCreateView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        form = CourseMaterialForm()
        return render(request, 'course_material/material_form.html', {'form': form})

    def post(self, request, course_id):
        form = CourseMaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.course = get_object_or_404(Course, id=course_id)
            material.created_by = request.user
            material.save()
            return redirect('course_material:material_list', course_id=course_id)
        return render(request, 'course_material/material_form.html', {'form': form})

class CourseMaterialUpdateView(LoginRequiredMixin, View):
    def get(self, request, material_id):
        material = get_object_or_404(CourseMaterial, id=material_id)
        form = CourseMaterialForm(instance=material)
        return render(request, 'course_material/material_form.html', {'form': form})

    def post(self, request, material_id):
        material = get_object_or_404(CourseMaterial, id=material_id)
        form = CourseMaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('course_material:material_list', course_id=material.course.id)
        return render(request, 'course_material/material_form.html', {'form': form})

class CourseMaterialDeleteView(LoginRequiredMixin, View):
    def get(self, request, material_id):
        material = get_object_or_404(CourseMaterial, id=material_id)
        return render(request, 'course_material/material_confirm_delete.html', {'material': material})

    def post(self, request, material_id):
        material = get_object_or_404(CourseMaterial, id=material_id)
        course_id = material.course.id
        material.delete()
        return redirect('course_material:material_list', course_id=course_id)
