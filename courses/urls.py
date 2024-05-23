from django.urls import path
from .views import (CourseListView, CourseDetailView, CourseCreateView, 
                    CourseUpdateView, CourseDeleteView, EnrollInCourseView)

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    
    path('<int:pk>/enroll/', EnrollInCourseView.as_view(), name='enroll_in_course'),
]
