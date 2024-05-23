from django.urls import path
from .views import (
    AssignmentListView,
    AssignmentDetailView,
    AssignmentCreateView,
    AssignmentUpdateView,
    AssignmentDeleteView,
    SubmissionCreateView,
    GradeAssignmentView
)

app_name = 'assignments'

urlpatterns = [
    path('', AssignmentListView.as_view(), name='assignment_list'),
    path('<int:pk>/', AssignmentDetailView.as_view(), name='assignment_detail'),
    path('create/', AssignmentCreateView.as_view(), name='assignment_create'),
    path('<int:pk>/update/', AssignmentUpdateView.as_view(), name='assignment_update'),
    path('<int:pk>/delete/', AssignmentDeleteView.as_view(), name='assignment_delete'),
    path('<int:pk>/submit/', SubmissionCreateView.as_view(), name='assignment_submit'),
    path('submission/<int:pk>/grade/', GradeAssignmentView.as_view(), name='assignment_grade'),
]
