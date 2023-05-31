from django.urls import path
from . import views

urlpatterns = [
    path('moliyaviy-malumotlar/', views.FinanceAPIView.as_view()),
    path('vacancy/', views.VacancyAPIView.as_view()),
    path('umumiy-ochiq/', views.CommonDataListAPIView.as_view()),
    path('axborot-olish-malumotlar/', views.GetInformationAPIView.as_view()),
    path('malumotlar-markazi/', views.InformationServiceAPIView.as_view()),
    path('davlat-organlari/', views.DavlatOrganlariAPIView.as_view()),
    path('markaz-hisobot/', views.CenterReportAPIView.as_view()),
    path('fuqarolar/', views.CitizenReportAPIView.as_view()),
]
