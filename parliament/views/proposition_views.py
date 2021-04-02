from django.shortcuts import render
from django.http import HttpResponse
from repository.repos import Deputy
from repository.repos import Proposition
from repository.repos import Legislature


def propositions_list(request):
    propositions = Proposition.get_all()
    context = {
        'propositions': propositions,
    }
    return render(request, 'parliament/pages/propositions.html', context)


def proposition_detail(request, pk):
    proposition = Proposition.get_one(pk)
    deputies_for = Deputy.get_all_voted_type_proposition(pk, 'for')
    deputies_against = Deputy.get_all_voted_type_proposition(pk, 'against')
    deputies_abstention = Deputy.get_all_voted_type_proposition(
        pk, 'abstention')
    deputies_absent = Deputy.get_all_voted_type_proposition(pk, 'absent')

    context = {
        'proposition': proposition,
        'deputies_for': deputies_for,
        'deputies_against': deputies_against,
        'deputies_abstention': deputies_abstention,
        'deputies_absent': deputies_absent
    }
    return render(request, 'parliament/pages/proposition.html', context)


def federal(request):
    propositions = Proposition.get_all_by_last_legislature_parliament('FED')
    deputies = Deputy.get_all_by_last_legislature_parliament('FED')
    legislature = Legislature.get_one_last_by_parliament('FED')
    context = {
        'propositions': propositions,
        'deputies': deputies,
        'legislature': legislature
    }
    return render(request, 'parliament/pages/federal.html', context)
