from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register_permier_emp, name='register'),
    path('register-employee', views.register_secondary_empolyee, name='register-employee'),
    path('check-email', views.check_email, name='check-email'),
    path('register-helper-emplyeer', views.register_helper_employee, name='register-helper'),
    path('register-needy', views.register_needy, name='register-needy'),
    path('register-donater', views.register_donator, name='register-donator'),
    path('register-volunteer', views.register_volunteer, name='register-volunteer'),
    path('user-profile', views.user_profile, name='user-profile'),
    path('user-profile-dash', views.user_profile_dash, name='user-profile-dash'),
    path('user-noti', views.get_notification, name='noti'),

]
