# Generated by Django 3.0 on 2019-12-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop', '0018_auto_20191215_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(null=True, upload_to='EShop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(null=True, upload_to='EShop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(null=True, upload_to='EShop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(null=True, upload_to='EShop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sales',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
