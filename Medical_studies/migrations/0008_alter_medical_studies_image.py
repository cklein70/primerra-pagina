# Generated by Django 4.1.4 on 2023-02-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medical_studies', '0007_rename_estpicture_medical_studies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_studies',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Medical_studies_images', verbose_name='imagen'),
        ),
    ]
