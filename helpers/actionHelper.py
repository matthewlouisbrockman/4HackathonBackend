import openaiHandler

def handleActionFromInput(input):
    systemMessage = {
        "role": "system",
        "content": """This is a JSON based adventure game. You return the JSON for the state changes on each action.
Each action is a JSON object with the following properties:
"narrative" - the text that is displayed to the user        
"actions" - an array of actions that the user can take
"state" - an object that contains the state of the game
"""
    }

    newMessage = {
        "role": "user",
        "content": input
    }

    return openaiHandler.queryChat(
        messages=[systemMessage, newMessage],
        max_tokens=400,
    )