from rest_framework import serializers
from .models import FinanceInformation, Vacancy, CenterReport, CitizenReport, CommonOpenData, InformationServiceContact, \
    GetInformation, DavlatOrganlari


class FinanceInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceInformation
        fields = ['id', 'title', 'content']


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'name', 'company', 'location', 'text', 'created_at']


class CommonOpenDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonOpenData
        fields = ['id', 'name', 'image', 'email', 'title', 'phone', 'address']


class GetInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInformation
        fields = ['id', 'title', 'content']


class InformationServiceContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationServiceContact
        fields = ['id', 'name', 'image', 'email', 'title', 'phone', 'address']


class DavlatOrganlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = DavlatOrganlari
        fields = ['id', 'title', 'content']


class CenterReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterReport
        fields = ['id', 'image', 'title', 'content', 'sub_title', 'sub_image', 'sub_content']


class CitizenReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenReport
        fields = ['id', 'image', 'title', 'content', 'sub_title', 'sub_image', 'sub_content']
