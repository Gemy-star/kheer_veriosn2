from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
    path('register-employee', views.register_empolyee, name='register-employee'),
    path('check-email', views.check_email, name='check-email'),

]
