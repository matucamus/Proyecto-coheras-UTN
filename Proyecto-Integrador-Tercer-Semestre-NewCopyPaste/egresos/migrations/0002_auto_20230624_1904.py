# Generated by Django 3.2.12 on 2023-06-24 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobante',
            name='fechaIngreso',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='fechaSalida',
            field=models.CharField(max_length=50),
        ),
    ]