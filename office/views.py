from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from office import models
from accounts.models import User


def home_employee(request):
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
        user_json = serializers.serialize('json', User.objects.filter(pk=pk))
        return JsonResponse(
            {"emp_count": emp_count, "cases_count": cases_count, "cases": cases_json, "foundation": found_json,
             "employee": user_json},
            content_type='application/json')


def create_needy(request):
    if request.method == 'GET':
        return render(request, 'office/add-needy.html')


def create_neeedy_ajax(request):
    if request.method == 'POST' and request.is_ajax:
        emp = request.user.pk
        emp_obj = User.objects.get(pk=emp)
        found_obj = models.Foundation.objects.get(employee=emp_obj)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        national_id = request.POST.get('national_id')
        depend_ages = request.POST.getlist('depend_ages[]')
        depend_genders = request.POST.getlist('depend_genders[]')
        depend_cases_type = request.POST.getlist('depend_cases_type[]')
        case_number = request.POST.get('case_number')
        case_age = request.POST.get('case_age')
        health_status = request.POST.get('health_status')
        source_type = request.POST.get('source_type')
        needy = models.Needy(name=name, national_id=national_id, phone=phone, home=address, health_status=health_status,
                             source_income=source_type, case_number=case_number, age=case_age)
        needy.save()
        found_obj.cases.add(needy)
        if len(depend_ages) == len(depend_genders) == len(depend_cases_type):
            for age in depend_ages:
                for gender in depend_genders:
                    for case_type in depend_cases_type:
                        depend = models.Dependency(age=age, gender=gender, stage=case_type)
                        depend.save()
                        needy.dependencies.add(depend)
        if needy.pk:
            return JsonResponse({"data": 1, "needy_Pk": needy.pk})
        else:
            return JsonResponse({"data": -1})


def needy_list(request):
    emp = request.user.pk
    emp_obj = User.objects.get(pk=emp)
    found_obj = models.Foundation.objects.get(employee=emp_obj)
    needies = found_obj.cases.all()
    context = {"needies": needies}
    return render(request, 'office/needy_list.html', context)


def needy_detial(request, pk):
    needy = models.Needy.objects.get(pk=pk)
    dep = needy.dependencies.all()
    context = {"needy": needy, "deps": dep}
    return render(request, 'office/needy_detail.html', context)


def delete_needy(request):
    if request.method == 'POST' and request.is_ajax:
        pk = request.POST.get('needy_id')
        needy = models.Needy.objects.get(pk=pk)
        if needy.delete():
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})
