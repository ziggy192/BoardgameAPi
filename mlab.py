#mongodb://<dbuser>:<dbpassword>@ds151008.mlab.com:51008/boardgame_hack
import mongoengine
import json

host = "ds151008.mlab.com"
port = 51008
db_name = "boardgame_hack"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


def list2json(l):
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    return json.loads(item.to_json())