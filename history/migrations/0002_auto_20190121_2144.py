# Generated by Django 2.1.5 on 2019-01-21 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='date_formed',
            field=models.IntegerField(verbose_name='date formed'),
        ),
    ]