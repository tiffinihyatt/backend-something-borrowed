from flask import Blueprint, request, jsonify, make_response, request
from app import db 
from app.models.Garment import Garment
from .helper_functions import get_available_garments, get_unavailable_garments

# board_bp = Blueprint('board_bp', __name__, url_prefix="/boards/")
garment_bp = Blueprint('garment_bp', __name__, url_prefix="/garments")

# get all available garments
@garment_bp.route("", methods=["GET"])
def get_all_garments():
    garments = Garment.query.all()
    garment_list = [garment.to_dict() for garment in garments]

    available_garments = get_available_garments(garment_list)

    return jsonify(available_garments)

# get garments in shopping bag
@garment_bp.route("/bag", methods=["GET"])
def get_shopping_bag():
    garments = Garment.query.all()
    garment_list = [garment.to_dict() for garment in garments]

    shopping_bag = get_unavailable_garments(garment_list)

    return jsonify(shopping_bag)

# create one new garment listing
@garment_bp.route("", methods=["POST"])
def create_garment():
    request_body = request.get_json()
    new_garment = Garment.create_instance_from_json(Garment, request_body)

    db.session.add(new_garment)
    db.session.commit()

    new_garment_dict = new_garment.to_dict()

    return new_garment_dict

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

    return make_response("Garment availability successfully updated", 200)


# delete one garment by id
@garment_bp.route("/<garment_id>", methods=["DELETE"])
def delete_garment(garment_id):
    garment = Garment.query.get(garment_id)

    db.session.delete(garment)
    db.session.commit()

    return make_response("Garment successfully deleted", 200)