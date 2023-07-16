from django.contrib import admin
from .models import *
from django import forms

class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ("contact_type",)
    search_fields = ("contact_type",)

    class Meta:
        verbose_name='Видове Контакт'


class ContactAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ContactAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'contact_note':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

    list_display = ("contact_title", "contact_phone_1", "contact_mail_1", "contact_type",)
    search_fields = ("contact_title", "contact_phone_1", "contact_mail_1", "contact_note",)

    class Meta:
        verbose_name='Контакти'

admin.site.register(ContactType, ContactTypeAdmin)
admin.site.register(Contact, ContactAdmin)