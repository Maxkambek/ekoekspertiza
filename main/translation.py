from modeltranslation.translator import register, TranslationOptions
from .models import News, NewsDetail, Spirituality, Management, Branch, Director, Partner, Document, CenterTarkibi


@register(Partner)
class PartnerTrans(TranslationOptions):
    fields = ('text',)


@register(Document)
class PartnerTrans(TranslationOptions):
    fields = ('title', 'month')


@register(Management)
class ManagementTranslation(TranslationOptions):
    fields = ('title', 'name', 'address', 'description')


@register(Branch)
class BranchTranslation(TranslationOptions):
    fields = ('name',)


@register(Director)
class DirectorTranslation(TranslationOptions):
    fields = ('title', 'name', 'address')


@register(CenterTarkibi)
class DirectorTranslation(TranslationOptions):
    fields = ('title', 'name', 'address')


@register(Spirituality)
class SpiritualityTranslation(TranslationOptions):
    fields = ('title', 'content')


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'subtitle', 'content')


@register(NewsDetail)
class NewsDetailTranslations(TranslationOptions):
    fields = ('content',)
