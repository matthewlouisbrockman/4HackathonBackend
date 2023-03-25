from flask import Flask, request
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

    return {'status': 'success', 'results': {'You kill the bear!'}}

if __name__ == "__main__":
    app.run()
