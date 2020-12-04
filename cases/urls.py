from django.urls import path
from . import views

urlpatterns = [
    path('create/contact', views.create_contact, name='create-contact'),
    path('add/needy-case', views.add_needycase, name='add-needycase'),
    path('payment/<int:pk>', views.payment_page, name='payment')

]
