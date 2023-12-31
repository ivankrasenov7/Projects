# Generated by Django 3.2.9 on 2022-03-16 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paintings',
            name='height',
            field=models.IntegerField(blank=True, verbose_name='Височина (см.)'),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='width',
            field=models.IntegerField(blank=True, verbose_name='Ширина (см.)'),
        ),
        migrations.AlterField(
            model_name='paintings',
            name='year',
            field=models.IntegerField(blank=True, verbose_name='Година'),
        ),
        migrations.AlterField(
            model_name='sculptures',
            name='year',
            field=models.IntegerField(blank=True, verbose_name='Година'),
        ),
    ]
