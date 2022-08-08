from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.Garment import Garment
from .routes_helper import get_available_garments


# board_bp = Blueprint('board_bp', __name__, url_prefix="/boards/")
garment_bp = Blueprint('garment_bp', __name__, url_prefix="/garments")

# get all available garments
@garment_bp.route("", methods=["GET"])
def get_all_garments():
    garments = Garment.query.all()
    garment_list = [garment.to_dict() for garment in garments]

    available_garments = get_available_garments(garment_list)

    return jsonify(available_garments)

# create one new garment listing
@garment_bp.route("", methods=["POST"])
def create_garment():
    request_body = request.get_json()
    new_garment = Garment.create_instance_from_json(Garment, request_body)

    db.session.add(new_garment)
    db.session.commit()

    return make_response("Garment successfully created", 201)

# get one garment by id
@garment_bp.route("/<garment_id>", methods=["GET"])
def get_garment_by_id(garment_id):
    garment = Garment.query.get(garment_id)
    return garment.to_dict()

# update availability on one garment
@garment_bp.route("/<garment_id>", methods=["PATCH"])
def toggle_availability(garment_id):
    garment = Garment.query.get(garment_id)
    garment.is_available = not garment.is_available

    db.session.commit()

    return make_response("Garment availability successfully updated", 201)