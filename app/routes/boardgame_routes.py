from flask import Blueprint, jsonify, abort, request, make_response
from app import db
from ..models.boardgame import Boardgame

bp = Blueprint("boardgames", __name__, url_prefix="/boardgames")

# POST /boardgames
@bp.route("", methods=("POST",))
def create_boardgame():
    request_body = request.get_json()
    boardgame = validate_boardgame(request_body)

    db.session.add(boardgame)
    db.session.commit()

    return jsonify(boardgame.to_dict()), 201
    
# GET /boardgames
@bp.route("", methods=("GET",))
def index_games():
    boardgames = Boardgame.query.all()

    result_list = [boardgame.to_dict() for boardgame in boardgames]

    return jsonify(result_list)

def validate_boardgame(id):
    boardgames = Boardgame.query.all()
    try:
        id = int(id)
    except ValueError:
        abort(make_response(jsonify(dict(details=f"invalid id: {id}")), 400))

    for game in boardgames:
        if game.id == id:
            # return the game
            return game

    # no game found
    abort(make_response(jsonify(dict(details=f"boardgame id {id} not found")), 404)) 