# Generated by Django 3.0.8 on 2020-12-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salida_Cabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SalCabFec', models.DateField(verbose_name='Fecha')),
            ],
            options={
                'verbose_name_plural': 'Salidas de productos',
            },
        ),
    ]
