# Generated by Django 4.1.4 on 2023-02-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appconsult', '0008_rename_picture_medical_speciality_mspicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_speciality',
            name='Description',
            field=models.CharField(max_length=200, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='medical_speciality',
            name='Medical_Speciality',
            field=models.CharField(max_length=40, verbose_name='Especialidad medica'),
        ),
    ]