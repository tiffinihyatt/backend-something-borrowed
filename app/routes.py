from flask import Blueprint, request, jsonify, make_response, render_template, request, redirect, send_file
from app import db 
from app.models.Garment import Garment
from .helper_functions import get_available_garments, upload_file
import os
from werkzeug.utils import secure_filename

# configurations for AWS S3
UPLOAD_FOLDER = "garment-images"
BUCKET = "something-borrowed-garments"

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

    new_garment_dict = new_garment.to_dict()

    return str(new_garment_dict["id"])

# upload one picture by garment id
@garment_bp.route("/<garment_id>/upload", methods=["POST"])
def upload_picture(garment_id):
    # access uploaded file
    file = request.files['file']

    # make new directory to store file
    directory = str(garment_id)
    path = os.path.join(UPLOAD_FOLDER, directory)
    os.mkdir(path)

    file.save(os.path.join(directory, secure_filename(file.filename)))
    upload_file(f"{directory}/{file.filename}", BUCKET)
    
    return make_response("Image successfully uploaded", 200)

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