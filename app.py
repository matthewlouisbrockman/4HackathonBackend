from flask import Flask, request, jsonify
from flask_cors import CORS

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

    return jsonify({'status': 'success', 'results': {'narrative':'You kill the bear!'}})

if __name__ == "__main__":
    app.run()
