import os
from django.db import models

# Maybe TODO / To See


class Party(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Parties"


class Legislature(models.Model):
    begin_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return "{0} - {1}".format(self.begin_date.strftime("%Y/%m"), self.end_date.strftime("%Y/%m"))


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
    title = models.CharField(max_length=255)
    date = models.DateField()
    legislature = models.ForeignKey(Legislature, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        print('hello save proposition')
        super().save(*args, **kwargs)
        from .repos.vote_repo import init_proposition_votes
        init_proposition_votes(self)
        print(self.id)

    def __str__(self):
        return '{} / {}'.format(self.title, self.legislature)


class Vote(models.Model):
    # TBD for | against | abstention | absent
    # Made other table for that?
    type_code = models.CharField(max_length=10)
    deputy = models.ForeignKey(Deputy, on_delete=models.CASCADE)
    proposition = models.ForeignKey(Proposition, on_delete=models.CASCADE)


# TODO bug with launch, it's call always twice
# For no production mode, rebuild the db to always have a 'clean' db
if os.environ.get('ENV') != 'PRODUCTION':
    from .repos.init_repo import init_db
    init_db()
