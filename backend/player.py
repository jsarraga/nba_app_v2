import sqlite3
from orm import ORM

DATABASE = "../data/nba.db"

class Player(ORM):
    dbpath = DATABASE
    tablename = 'players'
    fields = ['name', 'age', 'pos', 'user_pk']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')
        self.pos = kwargs.get('pos')
        self.user_pk = kwargs.get('user_pk')

    @classmethod
    def get_player(cls, name):
        with sqlite3.connect(DATABASE) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            SQL = "SELECT * FROM players WHERE name=?"
            cur.execute(SQL, (name,))
            player = cur.fetchone()
            if player is None:
                return None
            return cls(**player)

    