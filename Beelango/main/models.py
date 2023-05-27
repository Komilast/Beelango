from django.db import models


class Word(models.Model):
    _english = models.CharField(max_length=100, verbose_name='английское слово')
    _russian = models.JSONField(verbose_name='русские слова')
    _transcription = models.CharField(max_length=50, verbose_name='транскрипция')
    _synonyms = models.ManyToManyField('self', blank=True, verbose_name='синонимы')

    def __str__(self):
        return self.english

    @property
    def english(self):
        return self._english

    @english.setter
    def english(self, value):
        if value.isalpha() and value.isascii():
            self._english = value.capitalize()
        else:
            raise ValueError('Некорректное значение для английского слова')

    @property
    def russian(self):
        return self._russian

    @russian.setter
    def russian(self, value):
        for word in value:
            if not all(1040 <= ord(char) <= 1103 for char in word):
                raise ValueError('Некорректное значение для русского слова')
        self._russian = [word.capitalize() for word in value]

    @property
    def transcription(self):
        return self._transcription

    @transcription.setter
    def transcription(self, value):
        if not all(char.isalpha() and ord(char) < 128 for char in value):
            raise ValueError('Некорректное значение для транскрипции')
        self._transcription = f'[{value}]'

    @property
    def synonyms(self):
        return self._synonyms

    @synonyms.setter
    def synonyms(self, value):
        self._synonyms = value
