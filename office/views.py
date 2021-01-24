from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse
from office import models
from accounts.models import User
from cases.models import Certificate, NeedyCase, TamkeenSupply
from django.contrib.auth.decorators import login_required
from .filters import NeedyFilter, NeedyCaseFilter


@login_required(login_url='login')
def home_employee(request):
    user_obj = User.objects.get(pk=request.user.pk)
    request.session['user_id'] = user_obj.user_type
    return render(request, 'office/home-employee.html',{"user":user_obj})

def takafel_type(request):
    return render(request,'office/takafel_type.html')

def takafel_type_page(request,pk):
    needy = NeedyCase.objects.filter(case_type=pk)
    contexts = {"cases":needy , "case_type":pk}
    return render(request,'office/takafel_type_page.html',context=contexts)
    
def add_green_participant(request):
    if request.method == 'GET':
        founds = models.Foundation.objects.all()
        proivders = models.Provider.objects.all()
        users = User.objects.filter(user_type__range=(1, 4))
        return render(request , 'office/add-green-participant.html' , context={"emps": users , "providers":proivders , "founds":founds})
    elif request.method == 'POST' and request.is_ajax:
        emp = request.POST.get('emp')
        provider = request.POST.get('provider') 
        found = request.POST.get('found')
        emp_obj = User.objects.get(pk=emp)
        provid = models.Provider.objects.get(pk=provider)
        found_obj = models.Foundation.objects.get(pk=found)
        if models.GreenParticipant.objects.filter(participant=emp_obj).exists():
            green_obj = models.GreenParticipant.objects.get(participant=emp_obj)
            green_obj.provider = provid
            green_obj.foundation = found_obj
            return JsonResponse({"data":1})
        else:
            green = models.GreenParticipant(participant=emp_obj , provider=provid , foundation=found_obj)
            green.save()
            if green.pk:
                return JsonResponse({"data":1})
            else:
                return JsonResponse({"data":-1})

def add_course_bag(request):
    if request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        description = request.POST.get('description')
        link = request.POST.get('link')
        start = request.POST.get('start')
        end = request.POST.get('end')
        user = request.POST.get('user')
        user_obj = User.objects.get(pk=user)
        total = request.POST.get('total_hour')
        bag = models.CourseBag(
            name=name, description=description, link=link, start_date=start, end_date=end ,trainer=user_obj , total_hours=total)
        bag.save()
        if bag.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})
    return render(request, 'office/add-course_bag.html',context={"trainers":User.objects.filter(user_type=9)})

def bag_list(request):
    context = {"bags": models.CourseBag.objects.all()}
    return render(request, 'office/bag-list.html', context=context)


def bag_payment(request, pk):
    needs = models.Needy.objects.all()
    bag_obj = models.CourseBag.objects.get(pk=pk)
    user_obj = User.objects.get(pk=request.user.pk)
    if request.method == 'POST' and request.is_ajax:
        needy = request.POST.get('needy')
        needy_obj = models.Needy.objects.get(pk=needy)
        pay = models.PaymentCourseBag(
            user=user_obj, course=bag_obj, needy=needy_obj)
        pay.save()
        if pay.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})
    return render(request, 'office/payment-course_bag.html', context={"bag": bag_obj, "needs": needs})


def add_pay_ticket(request):
    needy = models.Needy.objects.all()
    context = {"needs": needy}
    if request.method == 'POST' and request.FILES['ticket']:
        vol = request.POST.get('needy')
        vol_obj = models.Needy.objects.get(pk=vol)
        ticket = request.FILES['ticket']
        fs = FileSystemStorage()
        filename = fs.save(ticket.name, ticket)
        ticket_obj = models.PayTicket(needy=vol_obj, ticket=ticket)
        ticket_obj.save()
        if ticket_obj is not None:
            return redirect('home-employee')
        else:
            return redirect('home-employee')
    return render(request, 'office/add-pay-ticket.html', context=context)


def add_bag_cer(request):
    needy = models.Needy.objects.all()
    bags = models.CourseBag.objects.all()
    context = {"needs": needy, "bags": bags}
    if request.method == 'POST' and request.FILES['cer']:
        vol = request.POST.get('needy')
        vol_obj = models.Needy.objects.get(pk=vol)
        bag = request.POST.get('bag')
        bag_obj = models.CourseBag.objects.get(pk=bag)
        cer = request.FILES['cer']
        fs = FileSystemStorage()
        filename = fs.save(cer.name, cer)
        ticket_obj = models.BagCertificate(
            needy=vol_obj, bag=bag_obj, certificate=cer)
        ticket_obj.save()
        if ticket_obj is not None:
            return redirect('home-employee')
        else:
            return redirect('home-employee')
    return render(request, 'office/add-bag-cer.html', context=context)


def get_emp_found_info(request):
    if request.method == 'GET' and request.is_ajax:
        pk = request.GET.get('user_id')
        user_obj = User.objects.get(pk=pk)
        user_json = serializers.serialize('json', User.objects.filter(pk=pk))
        if user_obj.user_type == 4:
            provider_obj = models.Provider.objects.filter(employee=user_obj)
            provider_json = serializers.serialize('json', provider_obj)
            return JsonResponse({"provider": provider_json, "employee": user_json}, content_type='application/json')
        elif user_obj.user_type == 7:
            certificates = Certificate.objects.filter(volunteer=user_obj)
            return JsonResponse({"volunteer": user_json}, content_type='application/json')
        else:
            found_obj = models.Foundation.objects.get(employee=user_obj)
            emp_count = found_obj.employee.count()
            cases_count = found_obj.cases.count()
            cases_all = found_obj.cases.all()
            found_count = models.Foundation.objects.all().count()
            cases_json = serializers.serialize('json', cases_all)
            found_json = serializers.serialize(
                'json', models.Foundation.objects.filter(employee=user_obj))
            return JsonResponse(
                {"emp_count": emp_count, "cases_count": cases_count, "cases": cases_json, "foundation": found_json,
                 "employee": user_json, "found_count": found_count},
                content_type='application/json')


@login_required(login_url='login')
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
        department = request.POST.get('department')
        support = request.POST.get('korba_type')
        emp_name = request.POST.get('emp_name')
        parent_name = request.POST.get('parent_name')
        enable_teen = request.POST.getlist('enable_teen[]')
        enable_needy = request.POST.get('enable_needy')
        job = request.POST.get('job')
        child_names = request.POST.getlist('child_names[]')

        needy = models.Needy(name=name, national_id=national_id, phone=phone, home=address, health_status=health_status,
                             source_income=source_type, case_number=case_number, age=case_age, department=department,
                             support=support,
                             emp_name=emp_name, enablity=enable_needy, job=job, parent=parent_name)
        needy.save()
        found_obj.cases.add(needy)
        if len(depend_ages) == len(depend_genders) == len(depend_cases_type) == len(enable_teen):
            for age in depend_ages:
                for gender in depend_genders:
                    for case_type in depend_cases_type:
                        for enable in enable_teen:
                            for child_name in child_names:
                                depend = models.Dependency(age=age, gender=gender, stage=case_type, enablity=enable,
                                                           name=child_name)
                                depend.save()
                                needy.dependencies.add(depend)

        if needy.pk:
            return JsonResponse({"data": 1, "needy_Pk": needy.pk})
        else:
            return JsonResponse({"data": -1})


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_needy(request):
    if request.method == 'POST' and request.is_ajax:
        pk = request.POST.get('needy_id')
        needy = models.Needy.objects.get(pk=pk)
        if needy.delete():
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


@login_required(login_url='login')
def delete_found(request):
    if request.method == 'POST' and request.is_ajax:
        pk = request.POST.get('found_id')
        found = models.Foundation.objects.get(pk=pk)
        if found.delete():
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


@login_required(login_url='login')
def found_list(request):
    founds = models.Foundation.objects.all()
    context = {"founds": founds}
    return render(request, 'office/found_list.html', context)


@login_required(login_url='login')
def found_detial(request, pk):
    found = models.Foundation.objects.get(pk=pk)
    emps = found.employee.all()
    cases = found.cases.all()
    context = {"found": found, "emps": emps, "cases": cases}
    return render(request, 'office/found_detail.html', context)


def enable_list(request):
    children = models.Dependency.objects.filter(enablity=1)
    enable_needies = models.Needy.objects.filter(enablity=1)
    context = {"children": children, "enable_needies": enable_needies}
    return render(request, 'office/enable_list.html', context=context)


@login_required(login_url='login')
def add_foundation(request):
    if request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        found = models.Foundation(
            name=name, address=address, phone=phone, description=description)
        found.save()
        if found.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})
    elif request.method == 'GET':
        return render(request, 'office/add-found.html', context={})


@login_required(login_url='login')
def add_provider(request):
    if request.method == 'GET':
        return render(request, 'office/add-provider.html', context={"emps": User.objects.filter(user_type=4)})
    elif request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        emp = request.POST.get('emps')
        emp_obj = User.objects.get(pk=emp)
        provider = models.Provider(
            name=name, address=address, phone=phone, description=desc, employee=emp_obj)
        provider.save()
        if provider.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


@login_required(login_url='login')
def provider_list(request):
    return render(request, 'office/provider-list.html', context={'providers': models.Provider.objects.all()})


@login_required(login_url='login')
def provider_delete(request):
    if request.method == 'POST' and request.is_ajax:
        provider_id = request.POST.get('provider_id')
        provid = models.Provider.objects.get(pk=provider_id)
        if provid.delete():
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


@login_required(login_url='login')
def home_emp(request):
    return render(request, 'office/enable-emp.html')


@login_required(login_url='login')
def add_course(request):
    if request.method == 'GET':
        context = {"cases": models.Needy.objects.filter(
            enablity=1), "provider": models.Provider.objects.all()}
        return render(request, 'office/add-course.html', context=context)
    elif request.method == 'POST' and request.is_ajax:
        course_name = request.POST.get('course_name')
        provider = request.POST.get('provider')
        provider_obj = models.Provider.objects.get(pk=provider)
        start = request.POST.get('start')
        end = request.POST.get('end')
        course_desc = request.POST.get('course_desc')
        cases = request.POST.getlist('cases[]')
        course = models.Courses(provider=provider_obj, description=course_desc,
                                name=course_name, start_date=start, end_date=end)
        course.save()
        for case in cases:
            case_obj = models.Needy.objects.get(pk=case)
            course.cases.add(case_obj)
        if course.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def search_needy_dash(request):
    need = models.Needy.objects.all()
    need_filter = NeedyFilter(request.GET, queryset=need)
    need = need_filter.qs
    context = {"neeedies": need, "myfilter": need_filter}
    return render(request, 'office/search-needy-dash.html', context)


def search_needy(request):
    needcases = NeedyCase.objects.all()
    need_filter = NeedyCaseFilter(request.GET, queryset=needcases)
    need = need_filter.qs
    context = {"neeedies": need, "myfilter": need_filter}
    return render(request, 'office/search-needy.html', context)


def cases_list(request):
    context = {"cases": NeedyCase.objects.all().order_by('case__data_added')}
    return render(request, 'office/cases-list.html', context=context)


def tamkeen_money(request):
    context = {"cases": TamkeenSupply.objects.all()}
    return render(request, 'office/tamkeen-money.html', context=context)
