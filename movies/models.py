import uuid

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Movie(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    synopsis = models.TextField()
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='movies/', null=True)
    release_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.title


def set_slug(sender, instance, *args, **kwargs):  # callback pre save
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Movie.objects.filter(slug=slug).exists():
            slug = slugify(
                f'{instance.title}-{str(uuid.uuid4())[:8]}'
            )
        instance.slug = slug


pre_save.connect(set_slug, sender=Movie)
