from django.shortcuts import render
from . import models
from django.http import JsonResponse
from accounts.models import User
from django.contrib.auth.decorators import login_required
from office.models import Needy, Dependency
from cases.models import VolunteerProfile, NeedyCase


@login_required(login_url='login')
def create_contact(request):
    if request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = models.Contact(name=name, address=address, phone=phone, message=message)
        contact.save()
        if contact.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


@login_required(login_url='login')
def add_needycase(request):
    if request.method == 'GET':
        return render(request, 'cases/add-needycase.html', context={"cases": Needy.objects.all()})
    elif request.method == 'POST' and request.is_ajax:
        case_pk = request.POST.get('case')
        case_obj = Needy.objects.get(pk=case_pk)
        case_type = request.POST.get('case_type')
        details = request.POST.get('details')
        st = models.NeedyCase.objects.filter(case=case_obj).exists()
        if st:
            st_obj = models.NeedyCase.objects.get(case=case_obj)
            st_obj.details = details
            st_obj.case_type = int(case_type)
            st_obj.save()
            return JsonResponse({"data": 1})
        else:
            obj = models.NeedyCase(details=details, case=case_obj, case_type=int(case_type))
            obj.save()
            if obj.pk:
                return JsonResponse({"data": 1})
            else:
                return JsonResponse({"data": -1})


@login_required(login_url='login')
def payment_page(request, pk):
    case_obj = Needy.objects.get(pk=pk)
    needycase_obj = models.NeedyCase.objects.get(case=case_obj)
    if request.method == 'GET':
        return render(request, 'cases/payment-page.html', context={"case": needycase_obj})
    elif request.method == 'POST' and request.is_ajax:
        user_id = request.user.pk
        user_obj = User.objects.get(pk=user_id)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        national_id = request.POST.get('national_id')
        ammount = request.POST.get('ammount')
        case_obj.case.total_donations = int(ammount)
        case_obj.case.amount = case_obj.case.amount - int(ammount)
        case_obj.case.save()
        payment_obj = models.Payment(name=name, phone=phone, address=address, national_id=national_id, helper=user_obj,
                                     case=case_obj, ammount=ammount)
        payment_obj.save()
        if payment_obj.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


@login_required(login_url='login')
def volunteer_page(request):
    user_obj = User.objects.get(pk=request.user.pk)
    context = {"certificates": models.Certificate.objects.filter(volunteer=user_obj)}
    return render(request, 'cases/home-volunteer.html', context=context)


def heba_kheer(request):
    if request.method == 'GET':
        return render(request, 'cases/heba-kheer.html')
    elif request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        national_id = request.POST.get('national_id')
        ammount = request.POST.get('ammount')
        heba_obj = models.HebaKheer(address=address, phone=phone, national_id=national_id, name=name, ammount=ammount)
        heba_obj.save()
        if heba_obj.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def add_tamkeen(request):
    context = {"needy": Needy.objects.filter(enablity=1), "depends": Dependency.objects.filter(enablity=1)}
    if request.method == 'GET':
        return render(request, 'cases/add-tamkeen.html', context=context)
    elif request.method == 'POST' and request.is_ajax:
        tamkeen_type = request.POST.get('tamkeen_type')
        person_type = request.POST.get('person_type')
        depend = request.POST.get('depend')
        need = request.POST.get('need')
        if int(person_type) == 1:
            dep = Dependency.objects.get(pk=depend)
            obj = models.TamkeenSupply(depend=dep, tamkeen_type=int(tamkeen_type))
            obj.save()
            if obj.pk:
                return JsonResponse({"data": 1})
            else:
                return JsonResponse({"data": -1})
        elif int(person_type) == 2:
            need_obj = Needy.objects.get(pk=need)
            obj_tamkeen = models.TamkeenSupply(case=need_obj, tamkeen_type=int(tamkeen_type))
            obj_tamkeen.save()
            if obj_tamkeen.pk:
                return JsonResponse({"data": 1})
            else:
                return JsonResponse({"data": -1})


def volunteer_list(request):
    volunteer_pro = VolunteerProfile.objects.filter(volunteer__user_type=7)
    return render(request, 'cases/volunteer_list.html', context={"vols": volunteer_pro})


def new_show_case(request):
    cases = NeedyCase.objects.all()
    context = {"cases": cases}
    return render(request, 'cases/new_case_show.html', context=context)
