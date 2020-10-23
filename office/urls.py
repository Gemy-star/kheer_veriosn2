from django.urls import path
from office import views

urlpatterns = [
    path('home-employee/<int:pk>', views.home_employee, name='home-employee'),
    path('get-found-emp-info', views.get_emp_found_info, name='get-found-emp-info'),
    path('create/needy', views.create_needy, name='create-needy')

]
