# Generated by Django 2.1.7 on 2020-02-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0033_auto_20200211_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provinceexecutive',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='provincejudiciary',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='provincialparliament',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True, unique=True),
        ),
    ]