# Generated by Django 2.2.5 on 2020-08-25 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeachApp', '0003_auto_20200821_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savecities',
            name='city_name',
            field=models.CharField(choices=[('Bora Bora', 'Bora Bora'), ('Kauai', 'Kauai'), ('Miami', 'Miami'), ('Barcelona', 'Barcelona'), ('Valparaiso', 'Valparaiso'), ('Sydney', 'Sydney'), ('Cape Town', 'Cape Town'), ('Singapore', 'Singapore'), ('Dubai', 'Dubai'), ('Los Angeles', 'Los Angeles')], max_length=75),
        ),
    ]