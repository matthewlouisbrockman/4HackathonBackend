import json
import openaiHandler
import db

def updateCombatAction(action, gameId):
    db.insertAction(action, "assistant", gameId)
    
    systemMessage = {
        "role": "system",
        "content": """This is a JSON based adventure game. You return the JSON for the state changes on each action.
Each response to the user action is a JSON object with the following properties:

interface Action {
  "narrative": string, // the text that is displayed to the user
  "possibleActions": string[], // an array of actions that the user can take
  "state": object // an object that contains the state of the game with at least {"location": string}
  "monsters": monster[] //an array of monsters that are in the location
}

interface monster {
  "name": string, // the name of the monster
  "level": number, // the level of the monster
  "type": string, // the type of the monster
}

- Do not worry if user input is not valid, the game will handle that, just make sure to return the correct JSON from the bot
- The JSON should have the keys in quotes as well so we can parse it easily
- The game should respond as if the user said things in the game, e.g. if the user says "what's up" the game should respond with "you said what's up, and [blah blah bla] depending on the state of the game"
- The user can choose to take one of the options or make up its own
- Make sure to give new results each time, especially after combat the defeated enemies should be gone.
- Be creative and detailed as possible.
"""
    }

    # startingAction = {
    #     "role": "assistant",
    #     "content": """{"state": {"location":"town"}, "narrative": "You are in a town. You can go to the forest or the mountains", "possibleActions": ["go to forest", "go to mountains"]}"""
    # }

    gameHistory = db.getActions(gameId)
    print('gameHistory: ', gameHistory)

    priorActions = []
    for action in gameHistory:
        if action['actor'] == 'assistant':
            priorActions.append({
                "role": "assistant",
                "content": action['content']
            })
        else:
            priorActions.append({
                "role": "user",
                "content": action['content']
            })

    lastAction = priorActions[-1]
    lastAction["content"] = lastAction['content'] + '\n\nHere is the new state and what can happen next. Provide a creative and detailed description! There should be no monsters now because they were defeated. Ensure the next response is properly formatted JSON.'


    res =  openaiHandler.queryChat(
        messages=[systemMessage] + priorActions,
        max_tokens=400,
    )

    print('res: ', res)

    parsedRes = json.loads(res[0])
    db.insertAction(parsedRes, "assistant", gameId)

    return parsedRes