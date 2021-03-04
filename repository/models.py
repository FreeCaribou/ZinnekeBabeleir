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

    def __str__(self):
        return '{} / {}'.format(self.title, self.legislature)


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

# Potentiel trigger
# TODO see how to init that with django, with query?

# BEGIN
# DECLARE bDone INT;
# DECLARE varId INT;
# DECLARE curs CURSOR FOR SELECT d.id FROM `repository_deputy` AS d, repository_deputy_legislatures AS dl WHERE d.id = dl.deputy_id AND dl.legislature_id = NEW.legislature_id;
# DECLARE CONTINUE HANDLER FOR NOT FOUND SET bDone = 1;

#  OPEN curs;
#   SET bDone = 0;
#   loop_c: LOOP
#     FETCH curs INTO varId;

#     IF bDone THEN
#     	LEAVE loop_c;
#     END IF;

# 	INSERT INTO `repository_vote` ( `type_code`, `deputy_id`, `proposition_id`)  VALUES ('wait', varId, NEW.id);

#   END LOOP;

#   CLOSE curs;

# END
