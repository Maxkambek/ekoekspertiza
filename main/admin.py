from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from .models import News, NewsDetail, Calculator, Spirituality, Branch, Management, Director, Document
from django.utils.translation import gettext_lazy as _


@admin.register(Document)
class A(TranslationAdmin):
    list_display = ['id', 'title', 'day', 'month', 'year']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class SpiritualityAdmin(TranslationAdmin):
    list_display = ['id', 'title']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class DirectorAdmin(TranslationAdmin):
    list_display = ['name', 'phone', 'title']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class BranchAdmin(TranslationAdmin):
    list_display = ['id', 'name']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ManagementAdmin(TranslationAdmin):
    list_display = ['id', 'name']
    list_filter = ['branch']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class NewsDetailInline(TranslationStackedInline):
    model = NewsDetail
    extra = 1

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class NewsAdmin(TranslationAdmin):
    inlines = [NewsDetailInline]
    list_display = ['id', 'title']
    search_fields = ['title', 'content']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.site_header = _('EcoExpertise Administration')
admin.site.index_title = _('Features area')  # default: "Site administration"
admin.site.site_title = 'eco administration'  # default: "Django site admin"

# admin.site.register(Spirituality, SpiritualityAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Calculator)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Director, DirectorAdmin)
