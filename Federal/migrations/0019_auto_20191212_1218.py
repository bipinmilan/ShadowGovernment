# Generated by Django 2.1.7 on 2019-12-12 06:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0018_auto_20191212_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]