from rest_framework import serializers
from .models import Movie

from reviews.serializers import ReviewModelSerielizer

class MovieModelSerielizer(serializers.ModelSerializer):
    reviews = ReviewModelSerielizer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = ["id", "title", "synopsis", "release_date", "image", "reviews"]
