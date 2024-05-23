from django.urls import path
from .views import CourseMaterialListView, CourseMaterialCreateView, CourseMaterialUpdateView, CourseMaterialDeleteView

app_name = 'course_material'

urlpatterns = [
    path('<int:course_id>/', CourseMaterialListView.as_view(), name='material_list'),
    path('create/<int:course_id>/', CourseMaterialCreateView.as_view(), name='material_create'),
    path('update/<int:pk>/', CourseMaterialUpdateView.as_view(), name='material_update'),
    path('delete/<int:pk>/', CourseMaterialDeleteView.as_view(), name='material_delete'),
]