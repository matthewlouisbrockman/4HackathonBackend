
"""
Schema

userid - ignore, fuck that (we'll want later)

1 table - games
gameid  uuid default uuid_generate_v4()
created_a timestamp default now()

1 table - actions
actionid uuid default uuid_generate_v4()
gameid uuid
created_a timestamp default now()
action text
actor text

1 table apicalls
apicallid uuid default uuid_generate_v4()
provider text
model text
latency float (ms)
created_a timestamp default now()
cost float

1 table images
imageid uuid default uuid_generate_v4()
gameid uuid
created_a timestamp default now()

"""

