# Generated by Django 4.2.6 on 2023-12-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goroskop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='star',
            name='foto',
        ),
        migrations.AddField(
            model_name='star',
            name='photo',
            field=models.ImageField(blank=True, upload_to='static/', verbose_name='Фото'),
        ),
    ]