# Generated by Django 4.1.4 on 2023-02-05 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appconsult', '0005_alter_index_options_professionals_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionals',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='prof_images', verbose_name='imagen'),
        ),
    ]