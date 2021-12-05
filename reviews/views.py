from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import ReviewModelSerielizer
from .models import Review

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