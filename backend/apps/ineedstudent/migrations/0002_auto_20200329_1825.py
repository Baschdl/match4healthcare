# Generated by Django 3.0.4 on 2020-03-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ineedstudent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='datenschutz_zugestimmt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hospital',
            name='einwilligung_datenweitergabe',
            field=models.BooleanField(default=False),
        ),
    ]
