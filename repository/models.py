import os
from django.db import models
from django.utils.html import mark_safe

# Maybe TODO / To See


class Party(models.Model):
    name = models.CharField(max_length=100)
    logo = models.BinaryField(editable=True, null=True)

    def __str__(self):
        return self.name

    def logo_tag(self):
        from base64 import b64encode
        return mark_safe('<img src = "data: image; base64, {}" height="100">'.format(
            b64encode(self.logo).decode('utf8')
        ))

    logo.short_description = 'Image'
    logo.allow_tags = True

    class Meta:
        verbose_name_plural = "Parties"


class Legislature(models.Model):
    begin_date = models.DateField()
    end_date = models.DateField(null=True)
    FEDERAL = 'FED'
    BRUSSELS = 'BRU'
    VLAAMS = 'VLA'
    WALLONIA = 'WAL'
    FRANCOPHONE = 'FRA'
    GERMANOPHONE = 'GER'
    SENAT = 'SEN'
    OTHER = 'other'
    PARLIAMENT_CHOICES = [
        (FEDERAL, 'federal'),
        (BRUSSELS, 'brussels'),
        (VLAAMS, 'vlaams'),
        (WALLONIA, 'wallonia'),
        (FRANCOPHONE, 'francophone'),
        (GERMANOPHONE, 'germanophone'),
        (SENAT, 'senat'),
        (OTHER, 'other')
    ]
    parliament = models.CharField(
        max_length=10,
        choices=PARLIAMENT_CHOICES,
        default=OTHER
    )

    def __str__(self):
        return "{} / {} - {}".format(self.parliament, self.begin_date.strftime("%Y/%m"), self.end_date.strftime("%Y/%m"))


class Deputy(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    legislatures = models.ManyToManyField(Legislature, related_name='deputies')

    def __str__(self):
        return '{} {} / {}'.format(self.first_name, self.last_name, self.party.name)

    class Meta:
        verbose_name_plural = "Deputies"


# Have proposition of vote different type?
class Proposition(models.Model):
    title_fr = models.CharField(max_length=255)
    title_nl = models.CharField(
        max_length=255, default=None, blank=True, null=True)
    detail = models.TextField(default=None, blank=True, null=True)
    date = models.DateField()
    legislature = models.ForeignKey(Legislature, on_delete=models.CASCADE)

    # if it's a new proposition, we must init the deputy vote
    # but not if it's an update!
    def save(self, *args, **kwargs):
        verify_id = self.id
        super().save(*args, **kwargs)
        if verify_id is None:
            from .repos.vote_repo import init_proposition_votes
            init_proposition_votes(self)

    def __str__(self):
        return '{} / {} --- {}'.format(self.title_fr, self.title_nl, self.legislature)


class Vote(models.Model):
    FOR = 'for'
    AGAINST = 'against'
    ABSTENTION = 'abstention'
    ABSENT = 'absent'
    WAIT = 'wait'
    CODE_CHOICES = [
        (FOR, 'for'),
        (AGAINST, 'against'),
        (ABSTENTION, 'abstention'),
        (ABSENT, 'absent'),
        (WAIT, 'wait')
    ]
    type_code = models.CharField(
        max_length=10,
        choices=CODE_CHOICES,
        default=WAIT
    )
    deputy = models.ForeignKey(Deputy, on_delete=models.CASCADE)
    proposition = models.ForeignKey(Proposition, on_delete=models.CASCADE)


# TODO bug with launch, it's call always twice
# For no production mode, rebuild the db to always have a 'clean' db
# if os.environ.get('ENV') != 'PRODUCTION':
#     from .repos.init_repo import init_db
#     init_db()
