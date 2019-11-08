from django.db import models
from polls.models.question import Question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

    @property
    def total_votes(self):
        return self.vote_set.count()
