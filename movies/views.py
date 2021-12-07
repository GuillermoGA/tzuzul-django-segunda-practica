from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from .models import Movie
from .serializers import MovieModelSerielizer


class MovieModelViewSet(ModelViewSet):
    serializer_class = MovieModelSerielizer
    queryset = Movie.objects.all()

    def get_queryset(self):
        filters_list = []

        # Search by title
        title = self.request.query_params.get('title')
        if title is not None:
            filters_list.append(Q(title__icontains=title))

        # Search by Category
        category_title = self.request.query_params.get('category')
        if category_title is not None:
            filters_list.append(Q(category__title__icontains=category_title))

        filters = Q()
        for filter in filters_list:
            filters = filters.__and__(filter)

        return Movie.objects.filter(filters)
