from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializer

class ReviewModelSerielizer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ["id", "title", "comment", "published_date", "stars", "movie", "user"]

    def __str__(self):
        return f"{self.movie.title} {self.title}"