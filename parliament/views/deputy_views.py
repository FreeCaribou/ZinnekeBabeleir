from django.shortcuts import render
from django.http import HttpResponse
from repository.repos import Deputy
from repository.repos import Proposition


def deputies_list(request):
    deputies_bru = Deputy.get_all_by_last_legislature_parliament('BRU')
    deputies_fed = Deputy.get_all_by_last_legislature_parliament('FED')
    deputies_vla = Deputy.get_all_by_last_legislature_parliament('VLA')
    deputies_wal = Deputy.get_all_by_last_legislature_parliament('WAL')
    deputies_fra = Deputy.get_all_by_last_legislature_parliament('FRA')
    deputies_ger = Deputy.get_all_by_last_legislature_parliament('GER')
    deputies_sen = Deputy.get_all_by_last_legislature_parliament('SEN')
    context = {
        'deputies_fed': deputies_fed,
        'deputies_bru': deputies_bru,
        'deputies_vla': deputies_vla,
        'deputies_wal': deputies_wal,
        'deputies_fra': deputies_fra,
        'deputies_ger': deputies_ger,
        'deputies_sen': deputies_sen
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
