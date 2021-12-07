from rest_framework import serializers

from categories.serializers import CategoryModelSerializer
from reviews.serializers import ReviewModelSerielizer
from .models import Movie


class MovieModelSerielizer(serializers.ModelSerializer):
    reviews = ReviewModelSerielizer(read_only=True, many=True)
    category = CategoryModelSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "synopsis", "release_date", "image", "reviews", "category"]
