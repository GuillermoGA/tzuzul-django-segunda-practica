import uuid

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

from categories.models import Category


class Movie(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    synopsis = models.TextField()
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    release_date = models.DateField(null=False, blank=False)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='movies')

    def __str__(self):
        return self.title
