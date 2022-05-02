from flask import Blueprint, jsonify, abort, request, make_response
from app import db
from ..models.boardgame import Boardgame

bp = Blueprint("boardgames", __name__, url_prefix="/boardgames")

def make_boardgame_safe(data_dict):
    try:
        return Boardgame.from_dict(data_dict)
    except KeyError as e:
        abort(make_response(jsonify(dict(details=f"missing required field: {e}")), 400))

# POST /cats
@bp.route("", methods=("POST",))
def create_cat():
    request_body = request.get_json()
    cat = make_boardgame_safe(request_body)

    db.session.add(cat)
    db.session.commit()

    return jsonify(cat.to_dict()), 201
    
# GET /cats

@bp.route("", methods=("GET",))
def index_boardgame():
    boardgames = Boardgame.query.all()

    result_list = [game.to_dict() for game in boardgames]

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

    # no cat found
    abort(make_response(jsonify(dict(details=f"boardgame id {id} not found")), 404))    

# GET /cats/id
@bp.route("/<id>", methods=("GET",))
def get_cat(id):
    cat = validate_boardgame(id)
    return jsonify(cat.to_dict())