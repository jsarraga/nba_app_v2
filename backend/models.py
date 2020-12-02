import sqlite3

DATABASE = "../data/nba.db"

where_clause = "SELECT * FROM {}"

def get_all_players():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        SQL = "SELECT * FROM players JOIN player_seasons ON players.pk = player_seasons.pk ORDER BY pts DESC"
        cur.execute(SQL)
        players = cur.fetchall()
        return players

#fix for most recent year
def get_by_stat(stat):
        with sqlite3.connect(DATABASE) as conn:
                cur = conn.cursor()
                SQL = """SELECT * FROM players JOIN player_seasons
                        ON players.pk = player_seasons.pk ORDER BY {} DESC""".format(stat)
                cur.execute(SQL)
                players = cur.fetchall()
                return players