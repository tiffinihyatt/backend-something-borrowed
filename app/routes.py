from flask import Blueprint, request, jsonify, make_response, abort
from app import db

# board_bp = Blueprint('board_bp', __name__, url_prefix="/boards/")
garment_bp = Blueprint('garment_bp', __name__, url_prefix="/garments")

