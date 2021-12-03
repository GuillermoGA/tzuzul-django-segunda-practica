from rest_framework import serializers
from .models import Movie


class MovieModelSerielizar(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "synopsis", "release_date", "image"]
