import json

import db

def updateCombatAction(action, gameId):
    db.insertAction(json.dumps(action), "assistant", gameId)
    