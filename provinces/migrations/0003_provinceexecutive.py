# Generated by Django 2.1.7 on 2019-12-26 08:33

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('offices', '0002_provincejudiciaryoffice'),
        ('provinces', '0002_auto_20191226_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvinceExecutive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('related_file', models.FileField(blank=True, upload_to='files/')),
                ('is_private', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.Category')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pro_ex_last_modified_by', to=settings.AUTH_USER_MODEL)),
                ('related_ministry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='offices.ExecutiveOffice')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]