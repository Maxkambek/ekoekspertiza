from modeltranslation.translator import TranslationOptions, register
from . import models


@register(models.FinanceInformation)
class FinanceInformationTrans(TranslationOptions):
    fields = ['title', 'content']


@register(models.Vacancy)
class VacancyTrans(TranslationOptions):
    fields = ['name', 'company', 'location', 'text']


@register(models.CommonOpenData)
class CommonOpenDataTrans(TranslationOptions):
    fields = ['name', 'title', 'address']


@register(models.GetInformation)
class GetInformationTrans(TranslationOptions):
    fields = ['title', 'content']


@register(models.InformationServiceContact)
class InformationServiceContactTrans(TranslationOptions):
    fields = ['name', 'title', 'address']


@register(models.DavlatOrganlari)
class DavlatOrganlariTrans(TranslationOptions):
    fields = ['title', 'content']


@register(models.CenterReport)
class DavlatOrganlariTrans(TranslationOptions):
    fields = ['title', 'content', 'sub_title', 'sub_content']


@register(models.CitizenReport)
class CitizenReportTrans(TranslationOptions):
    fields = ['title', 'content', 'sub_title', 'sub_content']
