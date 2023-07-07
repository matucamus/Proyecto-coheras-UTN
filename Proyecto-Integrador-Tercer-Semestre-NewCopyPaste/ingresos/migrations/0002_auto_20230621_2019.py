# Generated by Django 3.2.12 on 2023-06-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocheras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='ingreso',
            name='idCochera',
            field=models.IntegerField(default=0),
        ),
    ]
