from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from movies.models import Movie
from .models import Review
from .serializers import ReviewModelSerielizer


class ReviewModelViewSet(ModelViewSet):
    serializer_class = ReviewModelSerielizer
    queryset = Review.objects.all()

    def get_queryset(self):
        queryset = Review.objects.all()

        # Search By username
        username = self.request.query_params.get('username')
        if username:
            queryset = Review.objects.filter(user__username=username)
        return queryset

    def create(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated, ]

        # Get Movie
        movie = Movie.objects.filter(id=request.data["movie"]).first()
        review = Review.objects.create(
            title=request.data["title"],
            comment=request.data["comment"],
            stars=request.data["stars"],
            movie=movie,
            user=request.user,
        )

        review_serializer = ReviewModelSerielizer(review)
        return Response(review_serializer.data)
