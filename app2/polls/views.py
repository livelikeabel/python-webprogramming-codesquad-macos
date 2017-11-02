from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_qeustion_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_qeustion_list': latest_qeustion_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': q})

def results(request, question_id): #result page
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return redirect('polls:results', question_id = question.id)

def main(request):
    return HttpResponse("<h1>Hello, Codesquad</h1>")
