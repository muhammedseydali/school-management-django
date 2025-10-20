from django.urls import path
from . import views

urlpatterns = [
    path('add-student/', views.add_student, name='add-student'),
    path('student-list/', views.student_list, name='student-list'),
    path('edit-student/', views.edit_student, name='edit-student'),
    path('view-student/<slug:slug>/', views.view_student, name='student-details')
]
