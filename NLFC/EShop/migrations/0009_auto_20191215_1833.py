# Generated by Django 3.0 on 2019-12-15 13:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EShop', '0008_auto_20191213_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='', upload_to='EShop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='priceold',
            field=models.IntegerField(default=0, verbose_name=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.CharField(default='', max_length=30),
        ),
    ]