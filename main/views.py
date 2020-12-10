from django.shortcuts import render
from cases.models import NeedyCase


def home_page(request):
    context = {"cases": NeedyCase.objects.all().order_by('case__data_added')[:3]}
    return render(request, 'main/home.html', context=context)


def about_page(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')

def faq_question(request):
    return render(request, 'main/faq-questions.html')
