# Generated by Django 3.1.7 on 2021-06-23 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_auto_20210622_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
