# Generated by Django 2.2.7 on 2019-12-13 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EShop', '0006_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]