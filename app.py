import db

from flask import Flask, request, jsonify
from flask_cors import CORS


from helpers import actionHelper

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/generateNextMove", methods=['POST'])
def generateNextMove():

    requestJSON = request.get_json()

    gameId = requestJSON.get('gameId')
    playerInput = requestJSON.get('playerInput')

    formattedInput = f"""{{"playerAction": {playerInput}}}"""

    newAction = actionHelper.handleActionFromInput(formattedInput)
    return jsonify({'status': 'success', 'results': newAction})


@app.route("/startGame", methods=['POST'])
def start_game():

    default_game_start = {
        "state": {"location":"town"},
        "narrative": "You are in the woods, surrounded by trees. You can go to the forest or the mountains. Something moves in the bushes!",
        "possibleActions": ["investigate the bushes", "go to the mountains", "go to the forest"],
        "monsters": [
            {
                "name": "Rabid Squirril",
                "level": 0,
                "currentHealth": 0,
                "maxHealth": 5,
                "type": "Nature",
                "attacks": [
                    {
                        "name": "Bite",
                        "damage": 1,
                        "type": "physical"
                    }
                ]
            }]
    }

    gameId, _ = db.insertAction(default_game_start, None)

    return jsonify({'status': 'success', 'results': default_game_start, 'gameId': str(gameId)})

if __name__ == "__main__":
    app.run()
