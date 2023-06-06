from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password


class User(models.Model):
    username = models.CharField(
        max_length=20,
        unique=True,
        help_text='Обязательно к заполнению. Максимум 20 символов. Можно использовать буквы, цифры и символы @/./+/-/_',
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': 'Имя пользователя занято',
            'blank': 'Имя пользователя обязательно к заполнению',
            'max_length': 'Имя пользователя не может превышать 20 символов',
            'validators': 'Некорректное имя пользователя'
        },
        blank=False,
        null=False
    )

    email = models.EmailField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        validators=[validate_email],
        help_text='Обязательно к заполнению. Максимум 50 символов, минимум - 8',
        error_messages={
            'unique': 'Пользователь с такой электронной почтой уже существует',
            'blank': 'Электронная почта обязательна к заполнению',
            'max_length': 'Электронная почта не может превышать 50 символов',
            'validators': "Некорректная электронная почта"
        })

    password = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        help_text='Обязательно к заполнению. '
                  'Максимум 20 символов, минимум - 6. Можно использовать буквы, цифры, и символы @/./+/-/_',
        validators=[validate_password],
        error_messages={
            'blank': 'Пароль обязателен к заполнению',
            'max_length': 'Пароль не может превышать 20 символов',
            'validators': 'Введите корректный пароль'
        })

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)

    # todo В планах на будущее: Создать свои валидаторы
