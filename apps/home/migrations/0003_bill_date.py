# Generated by Django 3.2.6 on 2021-11-18 07:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211117_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
