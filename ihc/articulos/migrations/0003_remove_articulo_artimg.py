# Generated by Django 2.2.17 on 2020-12-20 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_auto_20201220_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='ArtImg',
        ),
    ]
