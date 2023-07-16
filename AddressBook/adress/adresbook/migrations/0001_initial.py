# Generated by Django 3.0.4 on 2021-03-07 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(max_length=100, verbose_name='Вид контакт')),
            ],
            options={
                'verbose_name_plural': 'Видове контакти',
                'ordering': ('contact_type',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_title', models.CharField(max_length=150, verbose_name='Име')),
                ('contact_phone_1', models.CharField(max_length=150, verbose_name='Телефон 1')),
                ('contact_phone_2', models.CharField(max_length=150, verbose_name='Телефон 2')),
                ('contact_mail_1', models.CharField(max_length=150, verbose_name='Електронен адрес 1')),
                ('contact_mail_2', models.CharField(max_length=150, verbose_name='Електронен адрес 2')),
                ('contact_note', models.CharField(max_length=255, verbose_name='Бележки')),
                ('contact_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adresbook.ContactType', verbose_name='Вид контакт')),
            ],
            options={
                'verbose_name_plural': 'Контакти',
                'ordering': ('contact_title',),
            },
        ),
    ]