from django.db import models

from random import choice
from string import ascii_letters, digits

SHORT_URL_SIZE = 7
AVAILABLE_CHARS = ascii_letters + digits

# Create your models here.

# модель - на основе ее создана таблица в базе данных
class URL(models.Model):
    created = models.DateTimeField(auto_now_add=True) # поле даты и времени создания записи
    times_followed = models.PositiveIntegerField(default=0) # поле для подсчета переходов по котроткой ссылке
    long_url = models.URLField() # поле для хранения длинной ссылки, введенной пользователем
    short_url = models.CharField(max_length=15, unique=True, blank=True) # поле для хранения кода короткой ссылки

    class Meta:
        ordering = ['-created']

    # метод, который определяет как таблица будет отображаться на сайте администрирования
    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    # метод создания короткой ссылки
    def create_short_url(self):
        url = ''
        for i in range(SHORT_URL_SIZE):
            url += choice(AVAILABLE_CHARS)
        # если сгенерировали ссылку, которая уже есть в таблице, то снова вызовем генерацию
        if URL.objects.filter(short_url=url).exists():
            self.create_short_url()

        self.short_url = url
            
