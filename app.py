from flask import Flask
import mlab
from mongoengine import *
from flask_restful import Resource, Api, reqparse

mlab.connect()

app = Flask(__name__)
api =  Api(app)

class Game(Document):
    title = StringField()
    content = StringField()


@app.route('/')
def hello_world():
    return 'Hello World!'


# class BoardgameList(Resource)
class Boardgame(Document):
    name = StringField()
    image = StringField()
    thumbnail = StringField()
    description = StringField()
    age = IntField()
    isFavorite = BooleanField()
    rule = StringField()
    minPlayers = IntField()
    maxPlayers = IntField()
    idealPlayers = IntField()
    playingTime = IntField()
    categories = ListField(StringField())
    mechanisms = ListField(StringField())


# b = Boardgame()
#
# b.categories = ["popular", "family"]
# b.name = "testGame"
# b.minPlayers = 1
# b.save()


parser = reqparse.RequestParser()
parser.add_argument("name", type=str, location="json")
parser.add_argument("image", type=str, location="json")
parser.add_argument("thumbnail", type=str, location="json")
parser.add_argument("age",type=int, location ="json")
parser.add_argument("description", type=str, location="json")
parser.add_argument("rule", type=str, location="json")
parser.add_argument("minPlayers", type=int, location="json")
parser.add_argument("maxPlayers", type=int, location="json")
parser.add_argument("idealPlayers", type=int, location="json")
parser.add_argument("playingTime", type=int, location="json")
parser.add_argument("isFavorite", type=bool, location="json")
parser.add_argument("categories", type=list, location="json")
parser.add_argument("mechanisms", type=list, location="json")

class BoardgameRes(Resource):
    def get(self):
        return mlab.list2json(Boardgame.objects)
    def post(self):
        args = parser.parse_args()
        name = args["name"]
        image = args["image"]
        thumbnail = args["thumbnail"]
        description = args["description"]
        age = args["age"]
        minPlayers = args["minPlayers"]
        maxPlayers = args["maxPlayers"]
        idealPlayers = args["idealPlayers"]
        playingTime = args["playingTime"]
        isFavorite = args["isFavorite"]
        categories = args["categories"]
        mechanisms = args["mechanisms"]

        new_boardgame = Boardgame()
        new_boardgame.name=name
        new_boardgame.image=image
        new_boardgame.thumbnail=thumbnail
        new_boardgame.age = age
        new_boardgame.description=description
        new_boardgame.minPlayers=minPlayers
        new_boardgame.maxPlayers=maxPlayers
        new_boardgame.idealPlayers=idealPlayers
        new_boardgame.playingTime=playingTime
        new_boardgame.isFavorite=isFavorite
        new_boardgame.categories=categories
        new_boardgame.mechanisms=mechanisms
        new_boardgame.save()
        return mlab.item2json(new_boardgame)
        # return {"code": 1, "status": "OK"}, 200

class BoargameSingleRes(Resource):
    def get(self,boardgame_id):
        all_games = Boardgame.objects
        found_game = all_games.with_id(boardgame_id)
        return mlab.item2json(found_game)

    def delete(self,boardgame_id):
        all_game = Boardgame.objects
        found_game = all_game.with_id(boardgame_id)
        found_game.delete()
        return {"code": 1, "status": "OK"}, 200
    def put(self,boardgame_id):
        args = parser.parse_args()
        name = args["name"]
        image = args["image"]
        thumbnail = args["thumbnail"]
        age = args["age"]
        description = args["description"]
        minPlayers = args["minPlayers"]
        maxPlayers = args["maxPlayers"]
        idealPlayers = args["idealPlayers"]
        playingTime = args["playingTime"]
        isFavorite = args["isFavorite"]
        categories = args["categories"]
        mechanisms = args["mechanisms"]

        # find note
        all_game = Boardgame.objects
        found_game = all_game.with_id(boardgame_id)

        #update
        found_game.name = name
        found_game.image = image
        found_game.thumbnail = thumbnail
        found_game.age = age
        found_game.description = description
        found_game.minPlayers = minPlayers
        found_game.maxPlayers = maxPlayers
        found_game.idealPlayers = idealPlayers
        found_game.playingTime = playingTime
        found_game.isFavorite = isFavorite
        found_game.categories = categories
        found_game.mechanisms = mechanisms
        found_game.save()

        return {"code": 1, "status": "OK"}, 200

api.add_resource(BoardgameRes, "/api/boardgame")
api.add_resource(BoargameSingleRes, "/api/boardgame/<boardgame_id>")

if __name__ == '__main__':
    app.run()

