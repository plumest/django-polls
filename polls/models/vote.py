from django.db import models
from polls.models.question import Question
from polls.models.choice import Choice
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class Vote(models.Model):
    """ A vote by a user """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # TODO: how to add a uniqueness constraint on database so is only one vote per (User, Question) pair.



