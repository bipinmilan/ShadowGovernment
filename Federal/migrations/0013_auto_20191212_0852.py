# Generated by Django 2.1.7 on 2019-12-12 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Federal', '0012_auto_20191212_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executive',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
