# Generated by Django 3.2.7 on 2021-09-10 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210910_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарий'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявление'},
        ),
    ]
