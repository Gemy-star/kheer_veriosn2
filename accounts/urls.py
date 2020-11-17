from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register_secondary_empolyee, name='register'),
    path('register-employee', views.register_secondary_empolyee, name='register-employee'),
    path('check-email', views.check_email, name='check-email'),
    path('register-helper-emplyeer', views.register_helper_employee, name='register-helper'),
    path('register-needy', views.register_needy, name='register-needy')

]
