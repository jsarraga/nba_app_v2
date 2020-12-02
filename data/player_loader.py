import csv
import sqlite3



def player_loader(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=",")
        data = []
        for row in reader:
            player_list = []
            stat_dict = {}
            name = row["Player"].split("\\")
            row["Player"] = name[0]
            stat_dict["name"] = row["Player"]
            stat_dict["age"] = row["Age"]
            stat_dict["pos"] = row["Pos"]
            player_list.append(stat_dict)
            data.append(player_list)
        return data

data1 = player_loader('raw_data/2018-2019.csv')

def player_load():
    with sqlite3.connect('nba.db') as connection:
        cur = connection.cursor()
        data = data1
        SQL = """ INSERT INTO players (name, age, pos) VALUES(?,?,?); """

        for item in data:
            for j in item:
                cur.execute(SQL, (j["name"], j["age"], j["pos"]))


if __name__ == "__main__":
    player_load()