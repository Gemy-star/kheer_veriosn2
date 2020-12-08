from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('about', views.about_page, name='about-page'),
    path('contact', views.contact, name='contact-page'),
    path('faq-questions', views.faq_question, name='faq'),

]
