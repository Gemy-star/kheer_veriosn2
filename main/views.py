from django.shortcuts import render


def home_page(request):
    return render(request, 'main/home.html')


def about_page(request):
    return render(request, 'main/about.html')
