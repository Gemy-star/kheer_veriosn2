from django.shortcuts import render
from cases.models import NeedyCase


def home_page(request):
    return render(request, 'main/home.html')


def about_page(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def faq_question(request):
    return render(request, 'main/faq-questions.html')


def ksa_2030(request):
    return render(request, 'main/ksa-2030.html')


def roaya_message(request):
    return render(request, 'main/roaya.html')


def tamkeen(request):
    return render(request, 'main/tamkeen.html')


def green_circle(request):
    return render(request, 'main/green-circle.html')


def pernamg(request):
    return render(request, 'main/pernamg.html')


def effect(request):
    return render(request, 'main/effect.html')
