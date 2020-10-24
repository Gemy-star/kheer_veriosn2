from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def check_email(request):
    if request.method == 'POST' and request.is_ajax:
        email = request.POST.get('email')
        user_obj = User.objects.get(email=email)
        if user_obj.pk:
            return JsonResponse(
                {"status": 1, "user_name": user_obj.first_name, "user_type": user_obj.user_type,
                 "email": user_obj.email})
        else:
            return JsonResponse({"status": 0})


def loginPage(request):
    if request.method == 'POST' and request.is_ajax:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.user_type == 2:
                login(request, user)
                return JsonResponse({"status": 'done', "user_pk": user.pk})
            else:
                login(request, user)
                return JsonResponse({"status": 'done', "user_pk": user.pk})


        else:
            return JsonResponse({"status": 'Username OR password is incorrect'})

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_volunteeruser(email=email, first_name=first_name, last_name=last_name,
                                                 address=address, password=password, phone=phone)
        if user is not None:
            if user.user_type == 2:
                login(request, user)
                return redirect('home-employee', user.pk)
            else:
                login(request, user)
                return redirect('home-employee', user.pk)


        else:
            messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
    context = {}
    return render(request, 'accounts/register.html', context)


def register_empolyee(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_employeeuser(email=email, first_name=first_name, last_name=last_name,
                                                address=address, password=password, phone=phone)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
    context = {}
    return render(request, 'accounts/register-employee.html', context)
