from django.shortcuts import render
from office.models import Needy
from . import models
from django.http import JsonResponse
from accounts.models import User


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


def add_needycase(request):
    if request.method == 'GET':
        return render(request, 'cases/add-needycase.html', context={"cases": Needy.objects.all()})
    elif request.method == 'POST' and request.is_ajax:
        case_pk = request.POST.get('case')
        case_obj = Needy.objects.get(pk=case_pk)
        case_type = request.POST.get('case_type')
        details = request.POST.get('details')
        needy_case = models.NeedyCase(details=details, case=case_obj, case_type=int(case_type))
        needy_case.save()
        if needy_case.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def payment_page(request, pk):
    user_id = request.user.pk
    user_obj = User.objects.get(pk=user_id)
    case_obj = models.NeedyCase.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'cases/payment-page.html', context={"user": user_obj, "case": case_obj})
    elif request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        national_id = request.POST.get('national_id')
        payment_method = request.POST.get('payment_method')
        ammount = request.POST.get('ammount')
        payment_obj = models.Payment(name=name, phone=phone, address=address, national_id=national_id, helper=user_obj,
                                     case=case_obj, payment_type=int(payment_method),ammount=ammount)
        payment_obj.save()
        if payment_obj.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})

