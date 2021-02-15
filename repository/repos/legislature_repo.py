from ..models import Legislature


def get_all():
    return Legislature.objects.all()
