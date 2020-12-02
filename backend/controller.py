from flask import Flask, jsonify, request
from flask_cors import CORS
from account import Account
import models, util

app = Flask(__name__)
CORS(app)


@app.route("/api/create", methods=["POST"])
def create_account():
    api_key = util.random_api_key()
    data = request.get_json()
    account = Account()
    account.username = data['username']
    password = data['password']
    hashed_pass = util.hash_password(password)
    account.api_key = api_key
    account.save()

@app.route("/all_players", methods=["GET"])
def get_players():
    players = models.get_all_players()
    player_list = []
    if players:
        for player in players:
            data = {}
            data["name"] = player[1]
            data["age"] = player[2]
            data["pos"] = player[3]
            data["sea"] = player[6]
            data["tm"] = player[8]
            data["pts"] = player[9]
            data["tpm"] = player[10]
            data["reb"] = player[11]
            data["ast"] = player[12]
            data["stl"] = player[13]
            data["blk"] = player[14]
            data["fgp"] = player[15]
            data["ftp"] = player[16]
            data["tov"] = player[17]
            data["g"] = player[18]
            data["gs"] = player[19]
            data["mp"] = player[20]
            player_list.append(data)
    else:
        data = {"name": "PLAYER NOT FOUND"}
    return jsonify(player_list)

@app.route("/all_players/<stat>", methods=["GET"])
def get_players_by_stat(stat):
    players = models.get_by_stat(stat)
    player_list = []
    if players:
        print(players)
        for player in players:
            data = {}
            data["name"] = player[1]
            data["age"] = player[2]
            data["pos"] = player[3]
            data["sea"] = player[6]
            data["tm"] = player[8]
            data["pts"] = player[9]
            data["tpm"] = player[10]
            data["reb"] = player[11]
            data["ast"] = player[12]
            data["stl"] = player[13]
            data["blk"] = player[14]
            data["fgp"] = player[15]
            data["ftp"] = player[16]
            data["tov"] = player[17]
            data["g"] = player[18]
            data["gs"] = player[19]
            data["mp"] = player[20]
            player_list.append(data)
    else:
        data = {"name" : "PLAYER NOT FOUND"}
    return jsonify(player_list)


if __name__ == "__main__":
    app.run(debug=True)