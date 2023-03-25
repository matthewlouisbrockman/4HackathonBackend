import json

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

    print('requestJSON: ', requestJSON)

    gameId = requestJSON.get('gameId')
    playerInput = requestJSON.get('playerInput')

    print('playerInput: ', playerInput)

    formattedInput = f"""{{"playerAction": {playerInput}}}"""


    newAction = actionHelper.handleActionFromInput(formattedInput)

    print('newAction: ', newAction)



    return jsonify({'status': 'success', 'results': newAction})

if __name__ == "__main__":
    app.run()
