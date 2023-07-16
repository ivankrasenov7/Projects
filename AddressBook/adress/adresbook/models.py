from django.db import models

class ContactType(models.Model):
    contact_type =  models.CharField(max_length=100, verbose_name='Вид контакт')

    def __str__(self):
        return self.contact_type

    class Meta:
        verbose_name = "Вид контакти"
        verbose_name_plural = "Видове контакти"
        ordering = ('contact_type',)

class Contact(models.Model):
    contact_title = models.CharField(max_length=150, verbose_name='Име')
    contact_phone_1 = models.CharField(max_length=150, verbose_name='Телефон 1')
    contact_phone_2 = models.CharField(max_length=150, verbose_name='Телефон 2', blank=True, default='')
    contact_mail_1 = models.CharField(max_length=150, verbose_name='Електронен адрес 1')
    contact_mail_2 = models.CharField(max_length=150, verbose_name='Електронен адрес 2', blank=True, default='')
    contact_type = models.ForeignKey(ContactType, on_delete=models.DO_NOTHING, verbose_name='Вид контакт')
    contact_note = models.CharField(max_length=255, verbose_name='Бележки')

    def __str__(self):
        return self.contact_title

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"
        ordering = ('contact_title',)