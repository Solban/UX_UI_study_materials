from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'isCorrect', 'createdOn', 'category')


class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Example
        fields = ('id', 'question', 'correct_answer_uri', 'wrong_answer_uri', 'correct_answer_explanation',
                  'wrong_answer_explanation', 'category')
