# Generated by Django 4.1.4 on 2023-02-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appconsult', '0004_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='index',
            options={'verbose_name': 'Imagen del Index ', 'verbose_name_plural': 'Imagenes del Index'},
        ),
        migrations.AddField(
            model_name='professionals',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='professionals '),
        ),
        migrations.AlterField(
            model_name='index',
            name='image_index',
            field=models.ImageField(blank=True, upload_to='index_images', verbose_name='imagenen index'),
        ),
    ]
