# Generated by Django 3.0.8 on 2020-09-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookrides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('pick_up', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
