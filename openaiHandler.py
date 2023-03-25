import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

def queryChat(messages: list, **kwargs) -> str:
    response = openai.ChatCompletion.create(
      messages=messages,
      model="gpt-3.5-turbo",
      **kwargs
    )


    return [choice['message']['content'] for choice in response['choices']]

def queryCompletion(prompt: str,  **kwargs) -> str:
    model = kwargs.get('model', 'text-davinci-003')
    response = openai.Completion.create(
      prompt=prompt,
      model=model,
      **kwargs
    )

    return [choice['text'] for choice in response['choices']]

def queryImage(prompt: str, userid: str, **kwargs):

    size = kwargs.get('size', '256x256')
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=size
    )

    return [{'url':url['url'] for url in response['data']}]
