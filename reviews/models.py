from django.db import models
from movies.models import Movie
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.TextField(max_length=100)
    comment = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    stars = models.PositiveIntegerField(max_length=5, default=0)

    movie = models.ForeignKey(Movie, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)