# Generated by Django 3.2.9 on 2021-12-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantsapi', '0004_plant_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
