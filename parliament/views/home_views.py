from django.shortcuts import render
from django.http import HttpResponse
from repository.repos import Deputy
from repository.repos import Proposition


def index(request):
    propositions_fed = Proposition.get_all_last_by_parliament('FED')
    # propositions_bru = Proposition.get_all_last_by_parliament('BRU')
    # propositions_vla = Proposition.get_all_last_by_parliament('VLA')
    # propositions_wal = Proposition.get_all_last_by_parliament('WAL')
    # propositions_fra = Proposition.get_all_last_by_parliament('FRA')
    # propositions_ger = Proposition.get_all_last_by_parliament('GER')
    # propositions_sen = Proposition.get_all_last_by_parliament('SEN')
    context = {
        'propositions_fed': propositions_fed
    }
    return render(request, 'parliament/pages/index.html', context)
