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
        "INSERT INTO {} (begin_date, end_date, parliament)".format(repo_legislature) +
        "VALUES('2015-01-01', '2020-01-01', 'BRU')" +
        ", ('2019-01-01', '2024-01-01', 'FED')" +
        ", ('2020-01-01', '2025-01-01', 'BRU')" +
        ", ('2020-01-01', '2025-01-01', 'VLA')" +
        ", ('2020-01-01', '2025-01-01', 'WAL')" +
        ", ('2020-01-01', '2025-01-01', 'FRA')" +
        ", ('2020-01-01', '2025-01-01', 'GER')"
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
        ",('6','2')" +
        ",('6','3')" +
        ",('6','4')" +
        ",('6','5')" +
        ",('6','6')" +
        ",('6','7')" +
        ",('2','3')" +
        ",('3','3')" +
        ",('3','4')" +
        ",('3','5')"
    )

    # <p align="center">Les frites c'est bien</p><p><br></p><p>Alors mettons en plus</p><p>Bisous</p><p><iframe data-youtube-id="IIaTdUkhEUE" src="https://www.youtube-nocookie.com/embed/IIaTdUkhEUE?wmode=opaque&amp;start=0" allowfullscreen="" width="560" height="315" frameborder="0"></iframe><br></p>

    cursor.execute(
        "INSERT INTO {} (title_fr, title_nl, date, legislature_id, detail)".format(repo_proposition) +
        "VALUES('Plus de frite à la cantine', 'Meer frietje', '2021-02-28', 2, '<p align=\"center\">Les frites c\\'est bien</p><p><br></p><p>Alors mettons en plus</p><p>Bisous</p><p><iframe data-youtube-id=\"IIaTdUkhEUE\" src=\"https://www.youtube-nocookie.com/embed/IIaTdUkhEUE?wmode=opaque&amp;start=0\" allowfullscreen=\"\" width=\"560\" height=\"315\" frameborder=\"0\"></iframe><br></p>')" +
        ", ('Mettre la chanson chef un petit verre on a soif du Lange Jojo comme hymne bruxellois', 'Een tof lied', '2021-02-16', 1, NULL)" +
        ", ('Un test', 'Een test', '2021-02-16', 2, NULL)" +
        ", ('2 test', '2 test', '2021-02-16', 2, NULL)" +
        ", ('3 test', '3 test', '2021-02-16', 2, NULL)" +
        ", ('4 test', '4 test', '2021-02-16', 2, NULL)" +
        ", ('5 test', '5 test', '2021-02-16', 2, NULL)"
    )

    cursor.execute(
        "INSERT INTO {} (type_code, deputy_id, proposition_id)".format(repo_vote) +
        "VALUES('for', 1, 1)" +
        ",('for', 1, 2)" +
        ",('against', 2, 1)" +
        ",('for', 3, 1)" +
        ",('against', 4, 1)" +
        ",('abstention', 5, 1)" +
        ",('absent', 6, 1)"
    )

    print('DB init finish')
