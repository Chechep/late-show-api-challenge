from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint('guest_bp', __name__, url_prefix='/guests')

@guest_bp.route('', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    return jsonify([{ "id": g.id, "name": g.name, "occupation": g.occupation } for g in guests])