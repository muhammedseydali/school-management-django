from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser, PasswordResetRequest
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User


def auth_home(request):
    return HttpResponse("Authentication Home")

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        role = request.POST.get('role', '').strip().lower()

        # Validate required fields
        if not (first_name and last_name and email and password and role):
            messages.error(request, "Please fill all required fields.")
            return redirect('signup')  # Replace with your signup URL name

        # Create user
        user = CustomUser.objects.create_user(
            username=email,  # Usually username is required, use email
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        # Assign role
        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True
        else:
            messages.error(request, "Invalid role selected.")
            return redirect('signup')

        user.save()

        # Log the user in
        login(request, user)
        messages.success(request, 'Signup successful!')
        return redirect('index')  # Replace with your home page URL name

    return render(request, 'authentication/register.html')



def login_view(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email', '').strip()
            password = request.POST.get('password', '').strip()

            if not email or not password:
                messages.error(request, "Please enter both email and password.")
                return redirect('login')  # Replace with your login URL name

            # Authenticate user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('index')  
            else:
                messages.error(request, "Invalid email or password.")
                return redirect('login')

        return render(request, 'authentication/login.html')  
    except Exception as e:
        # Log the error if needed
        messages.error(request, f"An unexpected error occurred: {str(e)}")
        return redirect('login')
    

def forget_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()

        if user:
            token = get_random_string(32)
            reset_request = PasswordResetRequest.objects.create(user=user, email=email, token=token)
            reset_request.send_reset_email()
            messages.success(request, 'reset password link sended to your mail')
        else:
            messages.error(request, 'email not found')
    return render(request, 'authentication/forget-password.html')

def reset_password_view(request, token):
    reset_request = PasswordResetRequest.objects.filter(token=token)

    if not reset_request or not reset_request.is_valid():
        messages.error("invalid or expired reset link")
        return redirect('index')
    
    if request.method == 'POST':
        new_password = request.POST['new_password']
        reset_request.user.set_password(new_password)
        reset_request.user.save()
        messages.success(request, 'password reset successfull')
        return redirect('login ')
    return render(request, 'reset_password.html', {'token': token})

def logout_view(request):
    logout(request)
    messages.success(request, 'you have been logged out')
    return redirect('index')