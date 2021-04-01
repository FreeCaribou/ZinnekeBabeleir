from django.shortcuts import render
from django.http import HttpResponse
from repository.repos import Deputy
from repository.repos import Proposition


def index(request):
    deputies = Deputy.get_all()
    propositions = Proposition.get_all()
    context = {
        'deputies': deputies,
        'propositions': propositions
    }
    return render(request, 'parliament/pages/index.html', context)
