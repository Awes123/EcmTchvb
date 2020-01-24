# Generated by Django 3.0 on 2019-12-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_detail',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_person', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
                ('mobile', models.CharField(default='', max_length=20)),
                ('Houseno', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=50)),
                ('Colony', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Account_User_ID',
            fields=[
                ('accre_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]