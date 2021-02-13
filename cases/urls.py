from django.urls import path
from . import views

urlpatterns = [
    path('create/contact', views.create_contact, name='create-contact'),
    path('add/needy-case', views.add_needycase, name='add-needycase'),
    path('payment/<int:pk>', views.payment_page, name='payment'),
    path('volunteer', views.volunteer_page, name='volunteer-page'),
    path('heba-kheer', views.heba_kheer, name='heba-kheer'),
    path('add-tamkeen', views.add_tamkeen, name='add-tamkeen'),
    path('volunteer-list', views.volunteer_list, name='volunteer-list'),
    path('all', views.new_show_case, name='show-all-cases'),
    path('technical-support', views.add_technical, name='technical-support'),
    path('technical-list', views.technical_list, name='technical-list'),
    path('show/report', views.CaseInShow.as_view(), name='case-show-pdf'),
    path('needy/all/report', views.NeedyAllReport.as_view(), name='needy-all-pdf'),
    path('found/all/report', views.FoundationAllReport.as_view(),
         name='found-all-pdf'),
    path('volunteer/all/report', views.VolunteerAllReport.as_view(),
         name='volunteer-all-pdf'),
    path('circles/all/report', views.GreenCircleAllReport.as_view(),
         name='circle-all-pdf'),
    path('enable/all/report', views.EnableAllReport.as_view(), name='enable-all-pdf'),
    path('volunteer/add/cer', views.add_vol_cer, name='add-vol-cer'),
    path('all/new', views.cases_all_new, name='cases-all-new'),
    path('types', views.cases_type, name='cases-types'),
    path('course/<int:pk>', views.pay_course_final, name='tamkeen-course-pay')
]
