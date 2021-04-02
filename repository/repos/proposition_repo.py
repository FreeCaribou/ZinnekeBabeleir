from ..models import Proposition, Vote
from django.shortcuts import get_object_or_404

# TBD for | against | abstention | absent


def get_all():
    p_list = Proposition.objects.all()
    for e in p_list:
        # e.votes = Vote.objects.filter(proposition=e)
        e = recup_vote_count(e)
    return p_list


def get_all_last_by_parliament(parliament, limit=5):
    return Proposition.objects.filter(legislature__parliament=parliament).order_by('-date')[0:limit]


def get_one(pk):
    p = get_object_or_404(Proposition, pk=pk)
    p.votes = Vote.objects.filter(proposition=p)
    p = recup_vote_count(p)
    return p


def get_all_for_deputy(deputy_pk):
    p_list = Proposition.objects.all().filter(vote__deputy_id=deputy_pk)
    for e in p_list:
        # I want here to see directly the type code of the deputy vote
        e.vote_type_code = Vote.objects.filter(
            proposition=e, deputy_id=deputy_pk).values('type_code').get()
        e.vote_type_code = e.vote_type_code['type_code']
    return p_list


def recup_vote_count(proposition):
    proposition.vote_count = Vote.objects.filter(proposition=proposition).count
    proposition.vote_for = Vote.objects.filter(
        proposition=proposition, type_code='for').count
    proposition.vote_against = Vote.objects.filter(
        proposition=proposition, type_code='against').count
    proposition.vote_abstention = Vote.objects.filter(
        proposition=proposition, type_code='abstention').count
    proposition.vote_absent = Vote.objects.filter(
        proposition=proposition, type_code='absent').count
    return proposition
