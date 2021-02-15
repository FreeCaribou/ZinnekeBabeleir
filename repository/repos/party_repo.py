from ..models import Party, Deputy
from django.shortcuts import get_object_or_404


def get_all():
    p_list = Party.objects.all()
    for e in p_list:
        e.deputies = Deputy.objects.filter(party=e)
    return p_list


def get_one(pk):
    p = get_object_or_404(Party, pk=pk)
    p.deputies = Deputy.objects.filter(party=p)
    return p
