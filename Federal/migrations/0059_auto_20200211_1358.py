# Generated by Django 2.1.7 on 2020-02-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0058_auto_20200211_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='judiciary',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='legislative',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
