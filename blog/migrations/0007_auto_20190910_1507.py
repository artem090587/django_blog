# Generated by Django 2.1.7 on 2019-09-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190909_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, db_index=True, upload_to='media/images', verbose_name='Изображение'),
        ),
    ]
