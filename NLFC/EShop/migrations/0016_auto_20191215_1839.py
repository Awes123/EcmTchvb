# Generated by Django 3.0 on 2019-12-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop', '0015_product_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='h', upload_to='EShop/images'),
        ),
    ]