from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import ReviewModelSerielizar
from .models import Review

class ReviewModelViewSet(ModelViewSet):
    serializer_class = ReviewModelSerielizar
    queryset = Review.objects.all()