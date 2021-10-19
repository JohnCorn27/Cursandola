# Generated by Django 3.2.7 on 2021-10-19 03:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_page_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('link', models.URLField(verbose_name='Link video')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
                'ordering': ['order', 'title'],
            },
        ),
        migrations.AddField(
            model_name='categoria',
            name='video',
            field=models.ManyToManyField(to='pages.Video'),
        ),
    ]