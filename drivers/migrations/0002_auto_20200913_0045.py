# Generated by Django 3.0.8 on 2020-09-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
