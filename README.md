# Game for 4 Hackathon

## install instructions

create venv

```
python3 -m venv venv
```

install requirements

```
pip install -r requirements.txt
```

run flask

```
FLASK_APP=app.py FLASK_DEBUG=true flask run
```

changes should autodeploy to heroku, not messing with branches cause we have 8 hrs
