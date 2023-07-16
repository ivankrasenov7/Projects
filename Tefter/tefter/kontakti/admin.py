from django.contrib import admin
from .models import *
from django import forms
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter


class ContactTypeAdmin(admin.ModelAdmin):
    search_fields = ('contact_type',)
    list_display =  ('contact_type',)


class ContactAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ContactAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'contact_note':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

    search_fields = ('contact_name', 'contact_phone_1', 'contact_phone_2', 'contact_mail_1', 'contact_mail_2', 'contact_note',)
    list_display = ('contact_name', 'contact_phone_1', 'contact_gender',)
    list_filter = ('contact_gender', ('contact_type', RelatedDropdownFilter),)


admin.site.register(ContactType, ContactTypeAdmin)
admin.site.register(Contacts, ContactAdmin)
