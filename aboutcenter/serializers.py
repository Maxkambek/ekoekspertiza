from rest_framework import serializers

from . import models


class DetailGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DetailGoal
        fields = ['id', 'text', 'image']


class GoalSerializer(serializers.ModelSerializer):
    detail_goal = DetailGoalSerializer(many=True)

    class Meta:
        model = models.GoalDirection
        fields = ['id', 'name', 'image_main', 'detail_goal']


class DetailLegalActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DetailLegalActivity
        fields = ['id', 'text', 'image']


class LegalActivitySerializer(serializers.ModelSerializer):
    legal_activity = DetailGoalSerializer(many=True)

    class Meta:
        model = models.LegalActivity
        fields = ['id', 'name', 'image_main', 'legal_activity']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HistoryCenter
        fields = ['id', 'image', 'title', 'content', 'image_2']


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ads
        fields = ['id', 'image', 'name', 'content', 'created_at']


class PoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Politics
        fields = ['id', 'image', 'title', 'content', 'image_2']


class ActivityIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActivityIndicator
        fields = ['id', 'image', 'name', 'content', 'title']


class InternationalContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InternationalContact
        fields = ['id', 'image', 'name', 'text']


class IntroCorruptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IntroCorruption
        fields = ['id', 'text']


class DetailCorruptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DetailCorruption
        fields = ['id', 'image', 'text']


class ConflictCorruptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConflictCorruption
        fields = ['id', 'text']


class FactorsCorruptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FactorsCorruption
        fields = ['id', 'image', 'text']


class HistoryCorruptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HistoryCorruption
        fields = ['id', 'name', 'text']


class CorruptionCrimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CorruptionCrimes
        fields = ['id', 'name', 'text']


class CorruptionCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CorruptionCases
        fields = ['id', 'text']


class CorruptionSerializer(serializers.ModelSerializer):
    cor_intro = IntroCorruptionSerializer(many=True)
    cor_detail = DetailCorruptionSerializer(many=True)
    cor_conflict = ConflictCorruptionSerializer(many=True)
    cor_factor = FactorsCorruptionSerializer(many=True)
    cor_history = HistoryCorruptionSerializer(many=True)
    cor_crime = CorruptionCrimesSerializer(many=True)
    cor_cases = CorruptionCasesSerializer(many=True)

    class Meta:
        model = models.Corruption
        fields = ['id', 'title', 'image',
                  'cor_intro', 'cor_detail', 'cor_conflict',
                  'cor_factor', 'cor_history', 'cor_crime', 'cor_cases'
                  ]
