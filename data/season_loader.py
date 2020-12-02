import csv
import sqlite3


def season_loader(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=",")
        data = []
        for row in reader:
            stat_list = []
            stat_dict = {}
            name = row["Player"].split("\\")
            row["Player"] = name[0]
            stat_dict["sea"] = "18-19"
            stat_dict["name"] = row["Player"]
            stat_dict["tm"] = row["Tm"]
            stat_dict["pts"] = row["PTS"]
            stat_dict["tpm"] = row["3P"]
            stat_dict["reb"] = row["TRB"]
            stat_dict["ast"] = row["AST"]
            stat_dict["stl"] = row["STL"]
            stat_dict["blk"] = row["BLK"]
            stat_dict["fgp"] = row["FG%"]
            stat_dict["ftp"] = row["FT%"]
            stat_dict["tov"] = row["TOV"]
            stat_dict["g"] = row["G"]
            stat_dict["gs"] = row["GS"]
            stat_dict["mp"] = row["MP"]
            stat_list.append(stat_dict)
            data.append(stat_list)
        return(data)

def load_season(filename):
    with sqlite3.connect('nba.db') as conn:
        cur = conn.cursor()
        new_data = season_loader(filename)

        SQL_insert = """ INSERT INTO player_seasons (sea, name, tm, pts, tpm, reb, ast,
                 stl, blk, fgp, ftp, tov, g, gs, mp) VALUES(?, ?, ?, ?, ?, ?, ?, ?,
                  ?, ?, ?, ?, ?, ?, ?); """

        for item in new_data:
            for j in item:
                name_matcher = j["name"]
                SQL = 'SELECT * FROM players WHERE name="{}"'.format(name_matcher)
                cur.execute(SQL)
                row = cur.fetchone()

                if row:
                    existing_player = row[1]
                    player_pk = row[0]
                    cur.execute(SQL_insert, (j["sea"], j["name"], j["tm"], j["pts"], j["tpm"], j["reb"],
                                j["ast"], j["stl"], j["blk"], j["fgp"], j["ftp"], j["tov"], j["g"],
                                j["gs"], j["mp"],))


        
load_season('raw_data/2018-2019.csv')
