from rest_framework import generics
from .models import GoalDirection, LegalActivity, HistoryCenter, Ads, Politics, ActivityIndicator, InternationalContact, \
    Corruption
from . import serializers


class GoalDirectionListAPIView(generics.ListAPIView):
    queryset = GoalDirection.objects.all()
    serializer_class = serializers.GoalSerializer


class LegalAPIView(generics.ListAPIView):
    queryset = LegalActivity.objects.all()
    serializer_class = serializers.LegalActivitySerializer


class HistoryAPIView(generics.ListAPIView):
    queryset = HistoryCenter.objects.all()
    serializer_class = serializers.HistorySerializer


class AdsListAPIView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = serializers.AdsSerializer


class PoliticsListAPIView(generics.ListAPIView):
    queryset = Politics.objects.all()
    serializer_class = serializers.PoliticsSerializer


class ActivityIndicatorAPIView(generics.ListAPIView):
    queryset = ActivityIndicator.objects.all()
    serializer_class = serializers.ActivityIndicatorSerializer


class InternationalContactAPIView(generics.ListAPIView):
    queryset = InternationalContact.objects.all()
    serializer_class = serializers.InternationalContactSerializer


class CorruptionAPIView(generics.ListAPIView):
    queryset = Corruption.objects.all()
    serializer_class = serializers.CorruptionSerializer
