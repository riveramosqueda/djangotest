# Generated by Django 3.2.9 on 2021-12-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_alter_mascota_vacuna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(blank=True, to='mascota.Vacuna'),
        ),
    ]
