# Generated by Django 2.1.7 on 2020-02-04 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0012_provincesname'),
    ]

    operations = [
        migrations.AddField(
            model_name='provinceexecutive',
            name='select_province',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='provinces.ProvincesName'),
        ),
        migrations.AddField(
            model_name='provincejudiciary',
            name='select_province',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='provinces.ProvincesName'),
        ),
        migrations.AddField(
            model_name='provincialparliament',
            name='select_province',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='provinces.ProvincesName'),
        ),
    ]