from ..models import Vote
from .deputy_repo import get_all_by_legislature


def get_all():
    return Vote.objects.all()


def init_proposition_votes(proposition):
    deputies = get_all_by_legislature(proposition.legislature.id)
    for d in deputies:
        v = Vote(type_code="wait", deputy=d, proposition=proposition)
        v.save()
