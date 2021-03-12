from ..models import Deputy
from django.shortcuts import get_object_or_404


def get_all():
    return Deputy.objects.all()


def get_one(pk):
    return get_object_or_404(Deputy, pk=pk)


# The list of deputies who have voted type for a propositon
def get_all_voted_type_proposition(proposition_pk, vote_type_code):
    return Deputy.objects.all().filter(vote__proposition__pk=proposition_pk, vote__type_code=vote_type_code)


def get_all_by_legislature(legislature_id):
    return Deputy.objects.all().filter(legislatures__pk=legislature_id).order_by('party__name', 'last_name', 'first_name')
