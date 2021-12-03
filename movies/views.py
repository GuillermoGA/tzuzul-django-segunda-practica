from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import MovieModelSerielizar
from .models import Movie

class MovieModelViewSet(ModelViewSet):
    serializer_class = MovieModelSerielizar
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = Movie.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = Movie.objects.filter(title__icontains=title)
        return queryset