import json
import openaiHandler

def handleActionFromInput(input):
    systemMessage = {
        "role": "system",
        "content": """This is a JSON based adventure game. You return the JSON for the state changes on each action.
Each response to the user action is a JSON object with the following properties:
"narrative" - the text that is displayed to the user        
"actions" - an array of actions that the user can take
"state" - an object that contains the state of the game

- Do not worry if user input is not valid, the game will handle that, just make sure to return the correct JSON from the bot
- The JSON should have the keys in quotes as well so we can parse it easily
- The game should respond as if the user said things in the game, e.g. if the user says "what's up" the game should respond with "you said what's up, and [blah blah bla] depending on the state of the game"
- The user can choose to take one of the options or make up its own
"""
    }

    startingAction = {
        "role": "assistant",
        "content": """{"state": {"location":"town"}, "narrative": "You are in a town. You can go to the forest or the mountains", "actions": ["go to forest", "go to mountains"]}"""
    }

    newMessage = {
        "role": "user",
        "content": input
    }

    res =  openaiHandler.queryChat(
        messages=[systemMessage, startingAction, newMessage],
        max_tokens=400,
    )

    res = json.loads(res[0])

    print('res: ', res)

    return res