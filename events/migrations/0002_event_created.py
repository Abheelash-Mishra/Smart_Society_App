# Generated by Django 4.2 on 2023-05-04 10:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
