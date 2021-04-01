from django.shortcuts import render
from django.http import HttpResponse
from repository.repos import Deputy
from repository.repos import Proposition


def deputies_list(request):
    deputies = Deputy.get_all()
    context = {
        'deputies': deputies,
    }
    return render(request, 'parliament/pages/deputies.html', context)


def deputy_detail(request, pk):
    deputy = Deputy.get_one(pk)
    propositions = Proposition.get_all_for_deputy(pk)

    context = {
        'deputy': deputy,
        'propositions': propositions
    }
    return render(request, 'parliament/pages/deputy.html', context)
