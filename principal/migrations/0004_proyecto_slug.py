# Generated by Django 3.1.1 on 2020-12-31 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_proyecto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
