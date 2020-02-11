from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
from django.utils.text import slugify
from categories.models import Category


class BaseModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=50, null=True, blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    related_file = models.FileField(upload_to='files/', blank=True)
    description = models.TextField(blank=False, null=True)
    is_private = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=False)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Set this model as Abstract

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BaseModel, self).save(*args, **kwargs)

