from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'dashboard'), name='logout'),
    path('signup', views.signupNavigator, name='signupNav'),
    path('doctorsignup', views.DoctorSignUp.as_view(), name='doctorSignup'),
    path('usersignup', views.UserSignUp.as_view(), name='userSignup')
]