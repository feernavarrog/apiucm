# Generated by Django 4.2.5 on 2024-03-22 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidop', models.CharField(max_length=50)),
                ('apellidom', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
            ],
        ),
    ]
