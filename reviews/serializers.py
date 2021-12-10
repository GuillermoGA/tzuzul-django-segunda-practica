from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Review


class ReviewModelSerielizer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "title", "comment", "published_date", "stars", "movie", "user"]

    def __str__(self):
        return f"{self.movie.title} {self.title}"
