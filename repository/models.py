import os
from django.db import models
from mysql.connector import connection

# Maybe TODO / To See


class Party(models.Model):
    name = models.CharField(max_length=100)


class Legislature(models.Model):
    begin_date = models.DateField()
    end_date = models.DateField(null=True)


class Deputy(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    legislatures = models.ManyToManyField(Legislature, related_name='deputies')


# Have proposition of vote different type?
class Proposition(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    legislature = models.ForeignKey(Legislature, on_delete=models.CASCADE)


class Vote(models.Model):
    # TBD for | against | abstention | absent
    # Made other table for that?
    type_code = models.CharField(max_length=10)
    deputy = models.ForeignKey(Deputy, on_delete=models.CASCADE)
    proposition = models.ForeignKey(Proposition, on_delete=models.CASCADE)


# TODO / To see another place? and bug with launch, it's call always twice
# For no production mode, rebuild the db to always have a 'clean' db
if os.environ.get('ENV') != 'PRODUCTION':
    print('ready to init DB?')
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SET foreign_key_checks = 0")
    cursor.execute("TRUNCATE TABLE `repository_party`")
    cursor.execute("TRUNCATE TABLE `repository_deputy`")
    cursor.execute("TRUNCATE TABLE `repository_legislature`")
    cursor.execute("TRUNCATE TABLE `repository_vote`")
    cursor.execute("TRUNCATE TABLE `repository_deputy_legislatures`")
    cursor.execute("TRUNCATE TABLE `repository_proposition`")
    cursor.execute("SET foreign_key_checks = 1")

    pl = Party(name="Left")
    pl.save()
    pr = Party(name="Right")
    pr.save()
    pc = Party(name="Center")
    pc.save()

    l1 = Legislature(begin_date="2015-01-01", end_date="2019-01-01")
    l1.save()

    l2 = Legislature(begin_date="2019-01-01", end_date="2023-01-01")
    l2.save()

    l3 = Legislature(begin_date="2011-01-01", end_date="2015-01-01")
    l3.save()

    plDOne = Deputy(first_name="Raoul", last_name="Estassis", party=pl)
    plDOne.save()
    plDOne.legislatures.add(l2, l1)

    plDTwo = Deputy(first_name="Sophie", last_name="Boonen", party=pl)
    plDTwo.save()
    plDTwo.legislatures.add(l2, l3)

    plROne = Deputy(first_name="Norman", last_name="Michel", party=pr)
    plROne.save()
    plROne.legislatures.add(l2)

    plRTwo = Deputy(first_name="Briton", last_name="Michel", party=pr)
    plRTwo.save()
    plRTwo.legislatures.add(l2)

    plCOne = Deputy(first_name="Olivier", last_name="Piedperdu", party=pc)
    plCOne.save()
    plROne.legislatures.add(l2)

    plCTwo = Deputy(first_name="Joëlle", last_name="Non", party=pc)
    plCTwo.save()
    plCTwo.legislatures.add(l2)

    plCThree = Deputy(first_name="Marxisme", last_name="Postfaon", party=pc)
    plCThree.save()
    plCThree.legislatures.add(l2)

    propOne = Proposition(title="Plus de frite à la cantine",
                          date="2021-02-16", legislature=l1)
    propOne.save()

    propTwo = Proposition(title="Mettre la chanson 'chef un petit verre on a soif' du Lange Jojo comme hymne bruxellois",
                          date="2021-02-28", legislature=l1)
    propTwo.save()

    vote = Vote(type_code="for", deputy=plDOne, proposition=propOne)
    vote.save()

    vote = Vote(type_code="for", deputy=plDTwo, proposition=propOne)
    vote.save()

    vote = Vote(type_code="for", deputy=plCOne, proposition=propOne)
    vote.save()

    vote = Vote(type_code="absent", deputy=plCTwo, proposition=propOne)
    vote.save()

    vote = Vote(type_code="abstention", deputy=plCThree, proposition=propOne)
    vote.save()

    vote = Vote(type_code="against", deputy=plROne, proposition=propOne)
    vote.save()

    vote = Vote(type_code="against", deputy=plRTwo, proposition=propOne)
    vote.save()

    print('DB init finish')