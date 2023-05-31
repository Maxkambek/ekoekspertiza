from rest_framework import serializers
from .models import News, NewsDetail, Calculator, Spirituality
from .models import Branch, Management, Director, Partner, Document, CenterTarkibi


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'day', 'month', 'year', 'file_path']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'image', 'text', 'link']


class SpiritualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Spirituality
        fields = ['id', 'image', 'title', 'content']


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetail
        fields = ['id', 'image', 'content', 'new']


class NewsSerializer(serializers.ModelSerializer):
    new_detail = NewsDetailSerializer(many=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'subtitle', 'image', 'content', 'created_at', 'new_detail']


class CalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculator
        fields = ['id', 'price']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'title', 'name', 'phone', 'email', 'image', 'address']


class CenterTarkibiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterTarkibi
        fields = ['id', 'title', 'name', 'phone', 'email', 'image', 'address']


class ManagementSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = Management
        fields = ['id', 'branch', 'title', 'name', 'phone', 'email', 'image', 'address', 'description']
