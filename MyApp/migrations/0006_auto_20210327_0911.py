# Generated by Django 3.1.7 on 2021-03-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_auto_20210327_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='discription',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]