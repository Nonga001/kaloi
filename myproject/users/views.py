from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = None  # Set role to None explicitly
            user.save()
            return redirect('login')  # Redirect to login or any other page
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    # Check the user's group and render the corresponding dashboard
    if request.user.groups.filter(name='students').exists():
        return render(request, 'student_dashboard.html')
    elif request.user.groups.filter(name='lecturers').exists():
        return render(request, 'lecturer_dashboard.html')
    else:
        return render(request, 'default_dashboard.html')
@login_required
def lecturer_dashboard(request):
    return render(request, 'lecturer_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def home(request):
    # You can pass any context to the template if needed
    context = {
        'user': request.user,  # You can pass the logged-in user data to the template
    }
    return render(request, 'home.html', context)

def profile(request):
    # You can pass the user details or other context to the template
    context = {
        'user': request.user,
    }
    return render(request, 'profile.html', context)

def enrollment(request):
    # Example view for enrollment
    context = {
        'user': request.user,
    }
    return render(request, 'enrollment.html', context)

def course(request):
    # Example view for course
    context = {
        'user': request.user,
    }
    return render(request, 'course.html', context)

