# Generated by Django 3.2.6 on 2021-11-25 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_bill_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Date',
            field=models.DateTimeField(blank=True, default=0),
        ),
    ]
