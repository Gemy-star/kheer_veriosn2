from django.shortcuts import render
from . import models
from cases.models import Contact


def home_page(request):
    return render(request, 'main/home.html')


def about_page(request):
    return render(request, 'main/about.html')


def who_page(request):
    return render(request, 'main/who-us.html')


def contact(request):
    return render(request, 'main/contact.html')


def ksa_shop(request):
    return render(request, 'main/shop-ksa.html')


def faq_question(request):
    context = {"faqs": models.FAQ.objects.all()}
    return render(request, 'main/faq-questions.html', context=context)


def ksa_2030(request):
    return render(request, 'main/ksa-2030.html')


def roaya_message(request):
    return render(request, 'main/roaya.html')


def tamkeen(request):
    return render(request, 'main/tamkeen.html')


def takafel(request):
    return render(request, 'main/takafel.html')


def green_circle(request):
    return render(request, 'main/green-circle.html')


def pernamg(request):
    return render(request, 'main/pernamg.html')


def effect(request):
    return render(request, 'main/effect.html')


def training(request):
    return render(request, 'main/training.html')


def ramadan(request):
    return render(request, 'main/ramdan.html')


def reports(request):
    return render(request, 'main/reports.html')
