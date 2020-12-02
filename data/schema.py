import sqlite3
import os 

DIR = os.path.dirname(__file__)
DBFILENAME = "nba.db"
DBPATH = os.path.join(DIR, DBFILENAME)

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        cur.execute(DROPSQL.format(tablename="accounts"))

        SQL = """CREATE TABLE accounts(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(16) NOT NULL,
                password VARCHAR(128),
                UNIQUE(username)
            ); """

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="players"))

        SQL = """ CREATE TABLE players(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            age VARCHAR,
            pos VARCHAR(5),
            user_pk INTEGER,
            FOREIGN KEY(user_pk) REFERENCES accounts(pk)
            ); """

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="player_seasons"))

        SQL = """ CREATE TABLE player_seasons(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            sea VARCHAR,
            name VARCHAR,
            tm VARCHAR,
            pts FLOAT,
            tpm FLOAT,
            reb FLOAT,
            ast FLOAT,
            stl FLOAT,
            blk FLOAT,
            fgp DECIMAL(18, 4),
            ftp DECIMAL(18, 4),
            tov FLOAT,
            g VARCHAR,
            gs VARCHAR,
            mp VARCHAR,
            player_pk INTEGER,
            FOREIGN KEY(player_pk) REFERENCES players(pk)
            ); """

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="watchlist"))

        SQL = """ CREATE TABLE watchlist(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            user_pk INTEGER,
            player_pk INTEGER,
            FOREIGN KEY(user_pk) REFERENCES accounts(pk),
            FOREIGN KEY(player_pk) REFERENCES players(pk)
            ); """

        cur.execute(SQL)


schema()
        
        