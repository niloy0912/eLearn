from django.urls import path
from .views import (CourseListView, CourseDetailView, CourseCreateView, 
                    CourseUpdateView, CourseDeleteView, EnrollCourseView, StudentCourseListView)

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='course_update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    
    # remove the enroll link if neededd
    path('<int:pk>/enroll/', EnrollCourseView.as_view(), name='enroll_in_course'),
    path('my-courses/', StudentCourseListView.as_view(), name='student_course_list'),
]
