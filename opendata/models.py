from django.db import models
from ckeditor.fields import RichTextField


class FinanceInformation(models.Model):
    class Meta:
        verbose_name = "Moliya to'g'risidagi ochiq ma'lumotlar"
        verbose_name_plural = "Moliya to'g'risidagi ochiq ma'lumotlar"

    title = models.TextField()
    content = RichTextField()

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    name = models.CharField(max_length=333)
    company = models.CharField(max_length=333)
    location = models.CharField(max_length=333)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bo'sh ish o'rinlari"
        verbose_name_plural = "Bo'sh ish o'rinlari"


class CommonOpenData(models.Model):
    class Meta:
        verbose_name = "Umumiy ochiq ma'lumotlarni joylashtirishga ma'sul shaxslar"
        verbose_name_plural = "Umumiy ochiq ma'lumotlarni joylashtirishga ma'sul shaxslar"

    name = models.CharField(max_length=212, verbose_name="Ismi")
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name='Email')
    title = models.CharField(max_length=250, verbose_name='Lavozimi')
    phone = models.CharField(max_length=70, verbose_name='Phone')
    address = models.CharField(max_length=223, verbose_name='Qabul kunlari')

    def __str__(self):
        return self.name


class GetInformation(models.Model):
    class Meta:
        verbose_name = "Axborot olishga doir so'rovlarni ko'rib chiqish"
        verbose_name_plural = "Axborot olishga doir so'rovlarni ko'rib chiqish"

    title = models.TextField()
    content = RichTextField()

    def __str__(self):
        return self.title


class InformationServiceContact(models.Model):
    class Meta:
        verbose_name = "Axborot xizmati bilan bog'lanish"
        verbose_name_plural = "Axborot xizmati bilan bog'lanish"

    name = models.CharField(max_length=212, verbose_name="Ismi")
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name='Email')
    title = models.CharField(max_length=250, verbose_name='Lavozimi')
    phone = models.CharField(max_length=70, verbose_name='Phone')
    address = models.CharField(max_length=223, verbose_name='Qabul kunlari')

    def __str__(self):
        return self.name


class DavlatOrganlari(models.Model):
    class Meta:
        verbose_name = "Davlat organlarining tasdiqlangan yillik ish rejalari"
        verbose_name_plural = "Davlat organlarining tasdiqlangan yillik ish rejalari"

    title = models.TextField()
    content = RichTextField()

    def __str__(self):
        return self.title


class CenterReport(models.Model):
    class Meta:
        verbose_name = "Markaz faoliyatiga oid hisobotlar"

        verbose_name_plural = "Markaz faoliyatiga oid hisobotlar"

    title = models.TextField()
    content = RichTextField()
    image = models.ImageField(upload_to='images/')
    sub_title = models.TextField(null=True, blank=True)
    sub_image = models.ImageField(upload_to='images/')
    sub_content = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title


class CitizenReport(models.Model):
    class Meta:
        verbose_name = "Fuqarolarning murojaatlari"
        verbose_name_plural = "Fuqarolarning murojaatlari"

    title = models.TextField()
    content = RichTextField()
    image = models.ImageField(upload_to='images/')
    sub_title = models.TextField(null=True, blank=True)
    sub_image = models.ImageField(upload_to='images/')
    sub_content = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title
