# Generated by Django 3.2.9 on 2021-12-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantsapi', '0003_alter_plant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100), max_length=100),
        ),
    ]
