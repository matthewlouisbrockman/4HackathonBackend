import os

import requests

ANTHORPIC_KEY = os.environ.get('ANTHORPIC_KEY')

def callClaude(prompt, **kwargs):

    formattedKwargs = {}
    for key, value in kwargs.items():
        if key == 'max_tokens':
            formattedKwargs['max_tokens_to_sample'] = value
        else:
            formattedKwargs[key] = value

    payload = {
        "prompt": 'Human: ' + prompt + '\n\nAssistant:',
        "model": "claude-v1",
        "stop_sequences": ["\n\nHuman:"],
        "max_tokens_to_sample": 300,
        **formattedKwargs
    }
    headers = {
        "x-api-key": ANTHORPIC_KEY,
        "content-type": "application/json"
    }
    r = requests.post("https://api.anthropic.com/v1/complete", json=payload, headers=headers)
    r = r.json()

    return r


def queryCompletion(prompt: str, userid: str, **kwargs) -> str:

    response = callClaude(prompt, **kwargs)

    return [response['completion']]
