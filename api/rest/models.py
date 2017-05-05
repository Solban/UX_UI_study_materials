from datetime import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Example(models.Model):
    question = models.CharField(max_length=500)
    correct_answer_uri = models.CharField(max_length=500)
    correct_answer_source = models.CharField(max_length=500, blank=True)
    wrong_answer_uri = models.CharField(max_length=500)
    wrong_answer_source = models.CharField(max_length=500, blank=True)
    correct_answer_explanation = models.CharField(max_length=500)
    wrong_answer_explanation = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Answer(models.Model):
    isCorrect = models.BooleanField()
    createdOn = models.DateTimeField(default=datetime.now, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
