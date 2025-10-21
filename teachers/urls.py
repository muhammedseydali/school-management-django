from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/<slug:slug>/', views.teacher_dashboard, name='teacher-dashboard'),
    path('teachers/', views.teacher_list, name='teacher-list'),
    path('teachers/add/', views.add_teacher, name='add-teacher'),
    path('teachers/edit/<slug:slug>/', views.edit_teacher, name='edit-teacher'),
    path('view/teacher/<slug:slug>/', views.view_teacher, name='teacher-details'),
    path('teachers/delete/<slug:slug>/', views.delete_teacher, name='delete-teacher'),
    path('teachers-dashboard/<slug:slug>/', views.teacher_dashboard, name='teacher-dashboard')
]
