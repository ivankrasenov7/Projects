from django.db import models


class ContactType(models.Model):
    contact_type = models.CharField(max_length=150, verbose_name="Вид контакт")

    def __str__(self):
        return self.contact_type

    class Meta:
        verbose_name = "Вид Контакт"
        verbose_name_plural = "Видове Контакти"
        ordering = ('contact_type',)


class Contacts(models.Model):

    GENDER_CHOICE = (
        ("f", "Жена"),
        ("m", "Мъж"),
    )

    contact_name = models.CharField(max_length=200, verbose_name="Име на контакт")
    contact_phone_1 = models.CharField(max_length=200, verbose_name="Телефон 1")
    contact_phone_2 = models.CharField(max_length=200, blank=True, verbose_name="Телефон 2")
    contact_mail_1 = models.CharField(max_length=200, verbose_name="Електронен адрес 1")
    contact_mail_2 = models.CharField(max_length=200, blank=True, verbose_name="Електронен адрес 2")
    contact_gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default="m", verbose_name="Пол")
    contact_type = models.ForeignKey(ContactType, on_delete=models.DO_NOTHING, verbose_name="Вид контакт")
    contact_note = models.CharField(max_length=350, blank=True, verbose_name="Бележки")

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"
        ordering = ('contact_name', )