# Generated by Django 4.2.6 on 2024-02-05 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goroskop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='photo',
            field=models.ImageField(blank=True, upload_to='static/images', verbose_name='Фото'),
        ),
    ]
