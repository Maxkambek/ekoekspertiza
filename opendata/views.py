from rest_framework import generics
from .models import FinanceInformation, Vacancy, CenterReport, CitizenReport, CommonOpenData, InformationServiceContact, \
    GetInformation, DavlatOrganlari
from . import serializers


class FinanceAPIView(generics.ListAPIView):
    queryset = FinanceInformation.objects.all()
    serializer_class = serializers.FinanceInformationSerializer


class VacancyAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = serializers.VacancySerializer


class CommonDataListAPIView(generics.ListAPIView):
    queryset = CommonOpenData.objects.all()
    serializer_class = serializers.CommonOpenDataSerializer


class GetInformationAPIView(generics.ListAPIView):
    queryset = GetInformation.objects.all()
    serializer_class = serializers.GetInformationSerializer


class InformationServiceAPIView(generics.ListAPIView):
    queryset = InformationServiceContact.objects.all()
    serializer_class = serializers.InformationServiceContactSerializer


class DavlatOrganlariAPIView(generics.ListAPIView):
    queryset = DavlatOrganlari.objects.all()
    serializer_class = serializers.DavlatOrganlariSerializer


class CenterReportAPIView(generics.ListAPIView):
    queryset = CenterReport.objects.all()
    serializer_class = serializers.CenterReportSerializer


class CitizenReportAPIView(generics.ListAPIView):
    queryset = CitizenReport.objects.all()
    serializer_class = serializers.CitizenReportSerializer
