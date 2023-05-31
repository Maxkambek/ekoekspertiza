from django.db import models
from ckeditor.fields import RichTextField


class Functions(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=223)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Funksiya va Vazifalari'
        verbose_name_plural = 'Funksiya va vazifalar'


class DetailFunctions(models.Model):
    function = models.ForeignKey(Functions, on_delete=models.CASCADE, related_name='detail_func')
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=450)
    content = RichTextField()
    sub_image = models.ImageField(upload_to='images/')
    sub_title = models.CharField(max_length=450)
    sub_content = RichTextField()

    def __str__(self):
        return self.title


class AnswerQuestions(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Ko'pincha so'raladigan savollar"
        verbose_name_plural = "Ko'pincha so'raladigan savollar"


class Xizmatlar(models.Model):
    text = models.TextField()

    def __str__(self):
        return f'{self.id}'
