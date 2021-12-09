from rest_framework.generics import ListAPIView

from .models import Category
from .serializers import CategoryModelSerializer


class CategoryListView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
