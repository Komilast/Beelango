from django.db import models


class Word(models.Model):
    english = models.CharField(max_length=100, verbose_name='английское слово')
    russian = models.TextField(verbose_name='русские слова')
    transcription = models.CharField(max_length=50, verbose_name='транскрипция')
    synonyms = models.ManyToManyField('self', blank=True, verbose_name='синонимы')

    def __str__(self):
        return self.english
