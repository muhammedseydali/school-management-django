from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('forget-password/', views.forget_password_view, name='forget_password'),
    path('reset_password/<str:token>/', views.reset_password_view, name='reset_password'),
    path('logout/', views.logout_view, name='logout')
]
