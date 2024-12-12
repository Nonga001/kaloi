from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  # Add this line
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),  # Profile page
    path('enrollment/', views.enrollment, name='enrollment'),  # Enrollment page
    path('course/', views.course, name='course'),  # Course page
    path('logout/', views.logout_view, name='logout'),  # Logout URL
]
