# Generated by Django 3.1.1 on 2020-12-30 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]