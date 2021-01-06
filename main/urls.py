from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('about', views.about_page, name='about-page'),
    path('contact', views.contact, name='contact-page'),
    path('faq-questions', views.faq_question, name='faq'),
    path('ksa-2030', views.ksa_2030, name='ksa2030'),
    path('roaya', views.roaya_message, name='roaya'),
    path('tamkeen', views.tamkeen, name='tamkeen'),
    path('green-circle', views.green_circle, name='green-circle'),
    path('pernamg', views.pernamg, name='pernamg'),
    path('effect', views.effect, name='effect'),
    path('training', views.training, name='training'),
    path('ramadan', views.ramadan, name='ramdan'),
    path('reports', views.reports, name='reports'),

]
