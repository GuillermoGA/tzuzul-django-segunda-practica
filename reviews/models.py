from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from movies.models import Movie


class Review(models.Model):
    title = models.TextField(max_length=100)
    comment = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    stars = models.PositiveIntegerField(null=False, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])

    movie = models.ForeignKey(Movie, null=False, blank=False, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"({self.movie.title}) {self.title}"
