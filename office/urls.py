from django.urls import path
from office import views

urlpatterns = [
    path('home-employee', views.home_employee, name='home-employee'),
    path('get-found-emp-info', views.get_emp_found_info, name='get-found-emp-info'),
    path('create/needy', views.create_needy, name='create-needy'),
    path('create/needy/ajax', views.create_neeedy_ajax, name='create-needy-ajax'),
    path('needy/list', views.needy_list, name='needy-list'),
    path('needy/detail/<int:pk>', views.needy_detial, name='needy-detail'),
    path('needy/delete', views.delete_needy, name='needy-delete'),
    path('found/delete', views.delete_found, name='found-delete'),
    path('found/detail/<int:pk>', views.found_detial, name='found-detail'),
    path('found/list', views.found_list, name='found-list'),
    path('enable/list', views.enable_list, name='enable-list'),
    path('found/add', views.add_foundation, name='add-found'),

]
