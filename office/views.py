from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from . import models
from accounts.models import User


def home_employee(request, pk):
    return render(request, 'office/home-employee.html')


def get_emp_found_info(request):
    if request.method == 'GET' and request.is_ajax:
        pk = request.GET.get('user_id')
        user_obj = User.objects.get(pk=pk)
        found_obj = models.Foundation.objects.get(employee=user_obj)
        emp_count = found_obj.employee.count()
        cases_count = found_obj.cases.count()
        cases_all = found_obj.cases.all()
        cases_json = serializers.serialize('json', cases_all)
        found_json = serializers.serialize('json', models.Foundation.objects.filter(employee=user_obj))
        user_json = serializers.serialize('json',  User.objects.filter(pk=pk))
        return JsonResponse(
            {"emp_count": emp_count, "cases_count": cases_count, "cases": cases_json, "foundation": found_json,
             "employee": user_json},
            content_type='application/json')


def create_needy(request):
    if request.method == 'POST' and request.is_ajax:
        found_id = request.POST.get('found_id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        national_id = request.POST.get('national_id')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        needy_obj = models.Needy(name=name, address=address, national_id=national_id, phone=phone,
                                 description=description)
        found_needy = models.Foundation.objects.get(pk=found_id)
        needy_obj.save()
        found_needy.cases.add(needy_obj)
        if needy_obj.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": 1})
