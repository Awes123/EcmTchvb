# Generated by Django 3.0 on 2019-12-15 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EShop', '0011_auto_20191215_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sprice',
        ),
    ]
