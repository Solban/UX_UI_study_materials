import django_filters
from rest_framework import viewsets, generics, filters

from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ExampleViewSet(viewsets.ModelViewSet):
    serializer_class = ExampleSerializer
    queryset = Example.objects.all()
    lookup_field = "category__name"
