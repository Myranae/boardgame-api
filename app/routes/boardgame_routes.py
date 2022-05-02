from flask import Blueprint, jsonify, abort, request, make_response
from app import db

bp = Blueprint("boardgames", __name__, url_prefix="/boardgames")

# POST /boardgames
@bp.route("", methods=("POST",))
def create_cat():
    request_body = request.get_json()
    cat = validate_boardgame(request_body)

    db.session.add(cat)
    db.session.commit()

    return jsonify(cat.to_dict()), 201
    
# GET /cats

@bp.route("", methods=("GET",))
def index_games():
    cats = Boardgames.query.all()

    result_list = [cat.to_dict() for cat in cats]

    return jsonify(result_list)

def validate_boardgame(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response(jsonify(dict(details=f"invalid id: {id}")), 400))

    for game in boardgames:
        if game.id == id:
            # return the cat
            return cat

    # no cat found
    abort(make_response(jsonify(dict(details=f"cat id {id} not found")), 404)) 