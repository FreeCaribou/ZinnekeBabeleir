from ..models import Deputy
from django.db.models import Q
from django.shortcuts import get_object_or_404
from repository.repos.legislature_repo import get_one_last_by_parliament


def get_all():
    return Deputy.objects.all()


def get_one(pk):
    return get_object_or_404(Deputy, pk=pk)


def get_all_filter_name(filter):
    return Deputy.objects.filter(Q(first_name__icontains=filter) | Q(last_name__icontains=filter))


def get_all_by_last_legislature_parliament(parliament):
    legislature = get_one_last_by_parliament(parliament)
    return Deputy.objects.all().filter(legislatures=legislature).order_by('party__name')


# The list of deputies who have voted type for a propositon
def get_all_voted_type_proposition(proposition_pk, vote_type_code):
    return Deputy.objects.all().filter(vote__proposition__pk=proposition_pk, vote__type_code=vote_type_code).order_by('party__name')


def get_all_by_legislature(legislature_id):
    return Deputy.objects.all().filter(legislatures__pk=legislature_id).order_by('party__name', 'last_name', 'first_name')
