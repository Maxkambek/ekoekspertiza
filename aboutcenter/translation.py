from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.GoalDirection)
class GoalDirectionTrans(TranslationOptions):
    fields = ['name', ]


@register(models.DetailGoal)
class DetailGoalTrans(TranslationOptions):
    fields = ['text', ]


@register(models.LegalActivity)
class LegalActivityTrans(TranslationOptions):
    fields = ['name', ]


@register(models.DetailLegalActivity)
class DetailLegalActivityTrans(TranslationOptions):
    fields = ['text', ]


@register(models.HistoryCenter)
class HistoryCenterTrans(TranslationOptions):
    fields = ['content', 'title']


@register(models.Ads)
class AdsTrans(TranslationOptions):
    fields = ['name', 'content']


@register(models.Politics)
class PoliticsTrans(TranslationOptions):
    fields = ['content', 'title']


@register(models.ActivityIndicator)
class ActivityIndicatorTrans(TranslationOptions):
    fields = ['name', 'content', 'title']


@register(models.InternationalContact)
class InternationalContactTrans(TranslationOptions):
    fields = ['name', 'text']


@register(models.Corruption)
class InternationalContactTrans(TranslationOptions):
    fields = ['title']


@register(models.IntroCorruption)
class InternationalTrans(TranslationOptions):
    fields = ['text']


@register(models.DetailCorruption)
class DetailCorruptionTrans(TranslationOptions):
    fields = ['text']


@register(models.ConflictCorruption)
class ConflictCorruptionTrans(TranslationOptions):
    fields = ['text']


@register(models.FactorsCorruption)
class FactorsCorruptionTrans(TranslationOptions):
    fields = ['text']


@register(models.HistoryCorruption)
class HistoryCorruptionTrans(TranslationOptions):
    fields = ['name', 'text']


@register(models.CorruptionCrimes)
class CorruptionCrimesTrans(TranslationOptions):
    fields = ['name', 'text']


@register(models.CorruptionCases)
class CorruptionCasesTrans(TranslationOptions):
    fields = ['text']
