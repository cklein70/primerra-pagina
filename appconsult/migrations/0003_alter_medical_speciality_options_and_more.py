# Generated by Django 4.1.4 on 2023-02-01 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appconsult', '0002_medical_speciality'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medical_speciality',
            options={'verbose_name': 'Especialidad Medica', 'verbose_name_plural': 'Especialidades Medicas'},
        ),
        migrations.AlterModelOptions(
            name='professionals',
            options={'verbose_name': 'Profesional', 'verbose_name_plural': 'Profesionales'},
        ),
        migrations.AlterField(
            model_name='professionals',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='speciality',
            field=models.CharField(max_length=40, verbose_name='especialidad'),
        ),
        migrations.AlterField(
            model_name='professionals',
            name='telehone',
            field=models.CharField(max_length=10, verbose_name='telefono'),
        ),
    ]