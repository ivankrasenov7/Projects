from django.db import models
from tinymce.models import HTMLField


class SculpType(models.Model):
    name = models.CharField(max_length=150, verbose_name='Вид')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид Скулптура'
        verbose_name_plural = 'Видове Скулптура'
        ordering = ('name',)


class PaintType(models.Model):
    name = models.CharField(max_length=150, verbose_name='Вид')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид Картина'
        verbose_name_plural = 'Видове Картини'
        ordering = ('name',)


class PaintGenre(models.Model):
    name = models.CharField(max_length=150, verbose_name='Вид')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр Картина'
        verbose_name_plural = 'Жанрове Картини'
        ordering = ('name',)


class Authors(models.Model):
    name = models.CharField(max_length=150, verbose_name='Автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'
        ordering = ('name',)


class Paintings(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заглавие')
    description = HTMLField(verbose_name='Описание на Картината')
    year = models.IntegerField(blank=True, verbose_name='Година')
    width = models.IntegerField(blank=True, verbose_name='Ширина (см.)')
    height = models.IntegerField(blank=True, verbose_name='Височина (см.)')
    author = models.ForeignKey(Authors, on_delete=models.DO_NOTHING, verbose_name='Автор')
    genre = models.ForeignKey(PaintGenre, on_delete=models.DO_NOTHING, verbose_name='Жанр')
    type = models.ForeignKey(PaintType, on_delete=models.DO_NOTHING, verbose_name='Вид')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картини'
        ordering = ('title',)


class Sculptures(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заглавие')
    description = HTMLField(verbose_name='Описание на Скулптурата')
    year = models.IntegerField(blank=True, verbose_name='Година')
    author = models.ForeignKey(Authors, on_delete=models.DO_NOTHING, verbose_name='Автор')
    type = models.ForeignKey(SculpType, on_delete=models.DO_NOTHING, verbose_name='Вид')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скулптура'
        verbose_name_plural = 'Скулптури'
        ordering = ('title',)
