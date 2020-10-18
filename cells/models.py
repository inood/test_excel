from django.db import models


class Cell(models.Model):
    column = models.CharField(max_length=1, verbose_name='Колонка')
    row = models.IntegerField(verbose_name='Строка')
    value = models.CharField(max_length=50, verbose_name='Значение')

    def __str__(self):
        return self.value
