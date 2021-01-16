from django.shortcuts import render, redirect
from django.template.loader import get_template
from datetime import datetime
from . import models
from django.http import JsonResponse
from accounts.models import User
from django.contrib.auth.decorators import login_required
from office.models import Needy, Dependency, Foundation
from cases.models import VolunteerProfile, NeedyCase, TechnicalSupport, TamkeenSupply
from django.http import HttpResponse
from django.views.generic import View
from kheer_new.utils import render_to_pdf
from django.core.files.storage import FileSystemStorage


@login_required(login_url='login')
def create_contact(request):
    if request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = models.Contact(
            name=name, address=address, phone=phone, message=message)
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
            obj = models.NeedyCase(
                details=details, case=case_obj, case_type=int(case_type))
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
    context = {"certificates": models.Certificate.objects.filter(
        volunteer=user_obj)}
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
        heba_obj = models.HebaKheer(
            address=address, phone=phone, national_id=national_id, name=name, ammount=ammount)
        heba_obj.save()
        if heba_obj.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def add_tamkeen(request):
    if request.method == 'POST' and request.is_ajax:
        tamkeen_type = request.POST.get('tamkeen_type')
        need = request.POST.get('need')
        need_obj = Needy.objects.get(pk=need)
        obj_tamkeen = models.TamkeenSupply(
            case=need_obj, tamkeen_type=int(tamkeen_type))
        obj_tamkeen.save()
        if obj_tamkeen.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})
    context = {"needy": Needy.objects.all()}
    return render(request, 'cases/add-tamkeen.html', context=context)


def volunteer_list(request):
    volunteer_pro = VolunteerProfile.objects.filter(volunteer__user_type=7)
    return render(request, 'cases/volunteer_list.html', context={"vols": volunteer_pro})


def new_show_case(request):
    cases = NeedyCase.objects.all()
    context = {"cases": cases}
    return render(request, 'cases/new_case_show.html', context=context)


def add_technical(request):
    user = User.objects.get(pk=request.user.pk)
    if request.method == 'GET':
        return render(request, 'main/technical-support.html')
    if request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        user_type = request.POST.get('user_type')
        message = request.POST.get('message')
        tech_support = TechnicalSupport(name=name, user_type=int(
            user_type), message=message, user=user)
        tech_support.save()
        if tech_support.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def technical_list(request):
    problems = TechnicalSupport.objects.all()
    return render(request, 'main/technical_list.html', context={"problems": problems})


class CaseInShow(View):
    def get(self, request, *args, **kwargs):
        template = get_template('case-in-show.html')
        needyinshow = NeedyCase.objects.all()
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "خير السعوديه",
            "user": user_obj,
            "needs": needyinshow,
            "topic": "الحالات المجهزة للعرض",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('case-in-show.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class NeedyAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('needy-all-pdf.html')
        needyinshow = Needy.objects.all()
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "خير السعوديه",
            "user": user_obj,
            "needs": needyinshow,
            "topic": "تفاصيل الحالات ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('needy-all-pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class EnableAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('enable-all-pdf.html')
        needyinshow = Needy.objects.filter(enablity=1)
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "خير السعوديه",
            "user": user_obj,
            "needs": needyinshow,
            "topic": "تفاصيل الحالات المرشحه للتمكين ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('enable-all-pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class FoundationAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('found-all-pdf.html')
        needyinshow = Foundation.objects.all()
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "خير السعوديه",
            "user": user_obj,
            "needs": needyinshow,
            "topic": "تفاصيل الجمعيات",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('found-all-pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class VolunteerAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('volunteer-all-pdf.html')
        needyinshow = VolunteerProfile.objects.all()
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "خير السعوديه",
            "user": user_obj,
            "needs": needyinshow,
            "topic": "تفاصيل المتطوعيين",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('volunteer-all-pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


def cases_all_new(request):
    context = {"tamkeen_cases": TamkeenSupply.objects.filter(tamkeen_type=2),
               "needy_cases": NeedyCase.objects.all()}
    return render(request, 'cases/cases-final-new.html', context=context)


def add_vol_cer(request):
    volunteers = User.objects.filter(user_type=7)
    context = {"volunteers": volunteers}
    if request.method == 'POST' and request.FILES['cer']:
        vol = request.POST.get('volunteer')
        vol_obj = User.objects.get(pk=vol)
        cer = request.FILES['cer']
        fs = FileSystemStorage()
        filename = fs.save(cer.name, cer)
        cer_obj = models.Certificate(volunteer=vol_obj, paper=cer)
        cer_obj.save()
        if cer_obj is not None:
            return redirect('home-employee')
        else:
            return redirect('home-employee')
    return render(request, 'cases/add-volunteer-certificate.html', context=context)
