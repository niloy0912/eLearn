from django.urls import path
from .views import GradeAssignmentView

app_name = 'grades'

urlpatterns = [
    path('grade/<int:assignment_id>/<int:student_id>/', GradeAssignmentView.as_view(), name='grade_assignment'),
]
