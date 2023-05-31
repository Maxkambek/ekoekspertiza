from django.db import models
from ckeditor.fields import RichTextField


class GoalDirection(models.Model):
    class Meta:
        verbose_name = "Maqsadi va yo'nalishlari"
        verbose_name_plural = "Maqsadi va yo'nalishlari"

    name = models.TextField(null=True, blank=True)
    image_main = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.id}'


class DetailGoal(models.Model):
    goal = models.ForeignKey(GoalDirection, on_delete=models.CASCADE, related_name='detail_goal')
    text = RichTextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = "Maqsadi va yo'nalishlari content"
        verbose_name_plural = "Maqsadi va yo'nalishlari content"

    def __str__(self):
        return f'{self.id}'


class LegalActivity(models.Model):
    class Meta:
        verbose_name = "Huquqiy faoliyat asoslari"
        verbose_name_plural = "Huquqiy faoliyat asoslari"

    name = models.TextField(null=True, blank=True)
    image_main = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.id}'


class DetailLegalActivity(models.Model):
    goal = models.ForeignKey(LegalActivity, on_delete=models.CASCADE, related_name='legal_activity')
    text = RichTextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = "Huquqiy faoliyat asoslari content"
        verbose_name_plural = "Huquqiy faoliyat asoslari content"

    def __str__(self):
        return f'{self.id}'


class HistoryCenter(models.Model):
    title = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = RichTextField()
    image_2 = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = 'Markaz Tarixi'
        verbose_name_plural = 'Markaz Tarixi'

    def __str__(self):
        return f'{self.id}'


class Ads(models.Model):
    name = models.CharField(max_length=1000)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "E'lonlar"
        verbose_name_plural = "E'lonlar"

    def __str__(self):
        return self.name


class Politics(models.Model):
    title = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = RichTextField()
    image_2 = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = 'Yoshlar siyosati'
        verbose_name_plural = 'Yoshlar siyosati'

    def __str__(self):
        return f'{self.id}'


class ActivityIndicator(models.Model):
    title = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    content = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Faoliyat Ko'rsatkichlari"
        verbose_name_plural = "Faoliyat Ko'rsatkichlari"


class InternationalContact(models.Model):
    class Meta:
        verbose_name = 'Xalqaro aloqalar'
        verbose_name_plural = 'Xalqaro aloqalar'

    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=500)
    text = RichTextField()

    def __str__(self):
        return self.name


class Corruption(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.id}'


class IntroCorruption(models.Model):
    corruption = models.ForeignKey(Corruption, on_delete=models.CASCADE, related_name='cor_intro')
    text = models.TextField()

    def __str__(self):
        return f'{self.corruption.id}'


class DetailCorruption(models.Model):
    corruption = models.ForeignKey(Corruption, on_delete=models.CASCADE, related_name='cor_detail')
    text = RichTextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.corruption.id}'


class ConflictCorruption(models.Model):
    text = models.TextField()
    corruption = models.ForeignKey(Corruption, on_delete=models.CASCADE, related_name='cor_conflict')

    def __str__(self):
        return f'{self.corruption.id}'


class FactorsCorruption(models.Model):
    text = models.TextField()
    corruption = models.ForeignKey(Corruption, on_delete=models.CASCADE, related_name='cor_factor')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.corruption.id}'


class HistoryCorruption(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    corruption = models.ForeignKey(Corruption, on_delete=models.CASCADE, related_name='cor_history')

    def __str__(self):
        return f'{self.corruption.id}'


class CorruptionCrimes(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    corruption = models.ForeignKey(Corruption, on_delete=models.CASCADE, related_name='cor_crime')

    def __str__(self):
        return f'{self.corruption.id}'


class CorruptionCases(models.Model):
    text = models.TextField()
    corruption = models.ForeignKey(Corruption, on_delete=models.CASCADE, related_name='cor_cases')

    def __str__(self):
        return f'{self.corruption.id}'
