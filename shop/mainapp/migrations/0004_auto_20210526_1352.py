# Generated by Django 3.1.7 on 2021-05-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210526_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='cd',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие SD карты'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объём встраиваемой памяти'),
        ),
    ]
