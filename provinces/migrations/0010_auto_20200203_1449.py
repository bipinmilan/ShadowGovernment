# Generated by Django 2.1.7 on 2020-02-03 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0009_provincialparliament'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provincialparliament',
            old_name='parliament_office',
            new_name='parliament_name',
        ),
    ]
