from django import template

register = template.Library()


@register.filter
def check_votes(choice, user):
    return choice.vote_set.filter(user=user).count()
