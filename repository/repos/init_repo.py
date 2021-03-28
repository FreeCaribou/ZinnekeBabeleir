def init_db():
    from django.db import connection
    print('ready to init DB?')
    repo_party = "repository_party"
    repo_deputy = "repository_deputy"
    repo_legislature = "repository_legislature"
    repo_vote = "repository_vote"
    repo_deputy_legislatures = "repository_deputy_legislatures"
    repo_proposition = "repository_proposition"

    cursor = connection.cursor()
    cursor.execute("SET foreign_key_checks = 0")
    cursor.execute("TRUNCATE TABLE {}".format(repo_party))
    cursor.execute("TRUNCATE TABLE {}".format(repo_deputy))
    cursor.execute("TRUNCATE TABLE {}".format(repo_legislature))
    cursor.execute("TRUNCATE TABLE {}".format(repo_vote))
    cursor.execute("TRUNCATE TABLE {}".format(repo_deputy_legislatures))
    cursor.execute("TRUNCATE TABLE {}".format(repo_proposition))
    cursor.execute("SET foreign_key_checks = 1")

    cursor.execute(
        "INSERT INTO {} (name) VALUES('Left'),('Right'),('Center') "
        .format(repo_party)
    )

    cursor.execute(
        "INSERT INTO {} (begin_date, end_date, parliament) VALUES('2015-01-01', '2019-01-01', 'FED'), ('2019-01-01', '2024-01-01', 'FED')"
        .format(repo_legislature)
    )

    cursor.execute(
        "INSERT INTO {} (first_name, last_name, party_id)".format(repo_deputy) +
        "VALUES('Raoul', 'Estassis', 1)" +
        ",('Norman', 'Michel', 2)" +
        ",('Sophie', 'Boonen', 1)" +
        ",('Briton', 'Michel', 2)" +
        ",('Olivier', 'Piedperdu', 3)" +
        ",('Joëlle', 'Ei', 3)"
    )

    cursor.execute(
        "INSERT INTO {} (deputy_id, legislature_id)".format(repo_deputy_legislatures) +
        "VALUES('1','1')" +
        ",('1','2')" +
        ",('2','2')" +
        ",('3','2')" +
        ",('4','2')" +
        ",('5','2')" +
        ",('6','1')" +
        ",('6','2')"
    )

    cursor.execute(
        "INSERT INTO {} (title_fr, title_nl, date, legislature_id)".format(repo_proposition) +
        "VALUES('Plus de frite à la cantine', 'Meer frietje', '2021-02-09', 2)" +
        ", ('Mettre la chanson chef un petit verre on a soif du Lange Jojo comme hymne bruxellois', 'Een tof lied', '2021-02-16', 2)"
    )

    cursor.execute(
        "INSERT INTO {} (type_code, deputy_id, proposition_id)".format(repo_vote) +
        "VALUES('for', 1, 1)" +
        ",('against', 2, 1)" +
        ",('for', 3, 1)" +
        ",('against', 4, 1)" +
        ",('abstention', 5, 1)" +
        ",('absent', 6, 1)"
    )

    print('DB init finish')
