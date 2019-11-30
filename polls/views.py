from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from polls.models.question import Question
from polls.models.choice import Choice
from polls.models.vote import Vote


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        find_vote = Vote.objects.filter(question=question, user=request.user)
        if find_vote.count() != 0:
            for user_vote in find_vote:
                user_vote.delete()
        new_vote = selected_choice.vote_set.create(question=question, choice=selected_choice, user=request.user)
        new_vote.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def reset_index(request):
    all_question_list = Question.objects.all()
    context = {'all_question_list': all_question_list}
    return render(request, 'polls/reset_polls.html', context)


def reset(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.reset_votes()
    messages.success(request, f'Reset votes for Poll \"{question.question_text}"')
    return HttpResponseRedirect(reverse('polls:reset_index'))
