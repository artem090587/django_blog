# Generated by Django 2.1.7 on 2019-09-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, db_index=True, height_field=500, upload_to='media', verbose_name='Изображение', width_field=1900),
        ),
    ]
