# Generated by Django 4.1.4 on 2023-02-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medical_studies', '0003_alter_medical_studies_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='medical_studies',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='est_images', verbose_name='imagen'),
        ),
    ]
