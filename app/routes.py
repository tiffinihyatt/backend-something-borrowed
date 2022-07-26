from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.Garment import Garment

# board_bp = Blueprint('board_bp', __name__, url_prefix="/boards/")
garment_bp = Blueprint('garment_bp', __name__, url_prefix="/garments")

# get all garments
@garment_bp.route("", methods=["GET"])
def get_all_garments():
    garments = Garment.query.all()
    garments_response = [garment.to_dict() for garment in garments]

    return jsonify(garments_response)

# create one new garment listing

# get one garment by id