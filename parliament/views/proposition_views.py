from django.shortcuts import render
from django.http import HttpResponse
from repository.repos import Deputy
from repository.repos import Proposition


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
