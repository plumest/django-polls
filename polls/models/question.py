import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def total_votes(self):
        """ Return the total number of votes for this poll question."""
        count_votes = 0
        for choice in self.choice_set.all():
            count_votes += choice.total_votes
        return count_votes

    def reset_votes(self):
        """ Resets the vote count to zero for all Choice for the Question."""
        for choice in self.choice_set.all():
            for vote in choice.vote_set.all():
                vote.delete()
            choice.save()

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
