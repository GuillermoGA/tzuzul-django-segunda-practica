from django.db import models
from movies.models import Movie


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # movies = models.ManyToOneRel(Movie)

    def __str__(self):
        return self.title
