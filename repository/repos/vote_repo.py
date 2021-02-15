from ..models import Vote


def get_all():
    return Vote.objects.all()
