# Generated by Django 4.2 on 2023-04-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact_no',
            field=models.CharField(default='N/A', max_length=13),
        ),
        migrations.AddField(
            model_name='profile',
            name='flat_no',
            field=models.CharField(default='N/A', max_length=6),
        ),
    ]
