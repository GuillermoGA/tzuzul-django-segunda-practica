from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import MovieModelSerielizer
from .models import Movie

class MovieModelViewSet(ModelViewSet):
    serializer_class = MovieModelSerielizer
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = Movie.objects.all()

        # Search by title
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = Movie.objects.filter(title__icontains=title)

        # Search by Category
        category_title = self.request.query_params.get('category')
        if category_title is not None:
            queryset = Movie.objects.filter(category__title__icontains=category_title)

        return queryset