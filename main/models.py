from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(max_length=222, verbose_name='Sarlavha')
    subtitle = models.CharField(max_length=333, null=True, blank=True, verbose_name="Qo'shimcha sarlavha")
    image = models.ImageField(upload_to='news', verbose_name='Rasm')
    content = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('Yangiliklar')
        verbose_name_plural = _('Yangiliklar')


class NewsDetail(models.Model):
    new = models.ForeignKey(News, on_delete=models.CASCADE, related_name='new_detail')
    image = models.ImageField(upload_to='news/', null=True)
    content = models.TextField(verbose_name=_('Yangilik contenti 2'), null=True)

    def __str__(self):
        return str(self.new.id)

    class Meta:
        verbose_name = "Yangilik 2-qism"
        verbose_name_plural = _('Yangilik 2-qism')


class Calculator(models.Model):
    price = models.PositiveIntegerField(verbose_name=_('Narx'))

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('Calculator')
        verbose_name_plural = _('Calculator')


class Spirituality(models.Model):
    image = models.ImageField(upload_to='Spirituality/', verbose_name=_('Rasm'))
    title = models.CharField(max_length=333, verbose_name=_('Sarlavha'))
    content = models.TextField(verbose_name=_('Content'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Maʼnaviyat va maʼrifat"
        verbose_name_plural = "Maʼnaviyat va maʼrifat"


class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Nomi'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Filiallar')
        verbose_name_plural = _('Filiallar')


class Management(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name=_('Filiallar'))
    name = models.CharField(max_length=212, verbose_name=_("Nomi"))
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name=_('Email'))
    title = models.CharField(max_length=250, verbose_name=_('Lavozimi'))
    phone = models.CharField(max_length=70, verbose_name=_('Phone'))
    address = models.CharField(max_length=223, verbose_name='Manzili')
    description = models.TextField(verbose_name='Filial haqida malumot')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hodimlar'
        verbose_name_plural = 'Hodimlar'


class Director(models.Model):
    name = models.CharField(max_length=212, verbose_name=_("Name"))
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name=_('Email'))
    title = models.CharField(max_length=250, verbose_name=_('Lavozimi'))
    phone = models.CharField(max_length=70, verbose_name=_('Phone'))
    address = models.CharField(max_length=223, verbose_name='Qabul kunlari')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Direktorlar')
        verbose_name_plural = _('Direktorlar')


class CenterTarkibi(models.Model):
    name = models.CharField(max_length=212, verbose_name=_("Name"))
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name=_('Email'))
    title = models.CharField(max_length=250, verbose_name=_('Lavozimi'))
    phone = models.CharField(max_length=70, verbose_name=_('Phone'))
    address = models.CharField(max_length=223, verbose_name='Qabul kunlari')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Markaz Tarkibi')
        verbose_name_plural = _('Markaz Tarkibi')


class Partner(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.CharField(max_length=123)
    link = models.URLField()

    def __str__(self):
        return self.text


class Document(models.Model):
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='documents')
    day = models.PositiveIntegerField()
    month = models.CharField(max_length=250)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    @property
    def file_path(self):
        return f"{settings.SITE_URL}{self.file.url}"
