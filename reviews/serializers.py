from rest_framework import serializers
from .models import Review


class ReviewModelSerielizar(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "title", "comment", "published_date", "stars", "movie", "user"]
