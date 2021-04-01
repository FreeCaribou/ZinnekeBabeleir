from ..models import Legislature


def get_all():
    return Legislature.objects.all()


def get_one_last_by_parliament(parliament):
    return Legislature.objects.filter(parliament=parliament).order_by('-begin_date').first()
