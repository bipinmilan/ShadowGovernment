# Generated by Django 2.1.7 on 2020-02-03 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0010_auto_20200203_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provincialparliament',
            old_name='parliament_name',
            new_name='related_parliament',
        ),
    ]
