# Generated by Django 3.0 on 2019-12-15 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EShop', '0012_remove_product_sprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sales',
        ),
    ]
