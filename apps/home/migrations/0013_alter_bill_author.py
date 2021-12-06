# Generated by Django 3.2.6 on 2021-12-05 10:47

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0012_bill_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='author',
            field=models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
