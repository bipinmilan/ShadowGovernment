# Generated by Django 2.1.7 on 2020-02-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0020_auto_20200209_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provinceexecutive',
            name='description',
            field=models.TextField(default=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='provincejudiciary',
            name='description',
            field=models.TextField(default=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='provincialparliament',
            name='description',
            field=models.TextField(default=False, max_length=200),
        ),
    ]