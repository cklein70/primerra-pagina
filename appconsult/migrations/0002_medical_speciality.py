# Generated by Django 4.1.4 on 2023-01-15 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appconsult', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medical_Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medical_Speciality', models.CharField(max_length=40)),
                ('Description', models.CharField(max_length=200)),
            ],
        ),
    ]