from django.urls import path
from .views import CourseMaterialListView, CourseMaterialCreateView, CourseMaterialUpdateView, CourseMaterialDeleteView

app_name = 'course_material'

urlpatterns = [
    path('<int:course_id>/', CourseMaterialListView.as_view(), name='material_list'),
    path('<int:course_id>/create/', CourseMaterialCreateView.as_view(), name='material_create'),
    path('update/<int:material_id>/', CourseMaterialUpdateView.as_view(), name='material_update'),
    path('delete/<int:material_id>/', CourseMaterialDeleteView.as_view(), name='material_delete'),
]
