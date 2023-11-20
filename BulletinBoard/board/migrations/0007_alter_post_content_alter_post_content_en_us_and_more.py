# Generated by Django 4.2.4 on 2023-11-17 09:47

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_comment_accepted_alter_comment_comment_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_en_us',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Контент'),
        ),
    ]
