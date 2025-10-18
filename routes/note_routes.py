from flask import Blueprint, request, jsonify
from extensions import db
from models import Note
from flask_jwt_extended import jwt_required, get_jwt_identity

note_bp = Blueprint('notes', __name__)


@note_bp.route('/', methods=['POST'])
@jwt_required()
def add_note():
    data = request.get_json()
    user_id = int(get_jwt_identity())
    note = Note(content=data['content'], user_id=user_id)
    db.session.add(note)
    db.session.commit()
    return jsonify({"message": "Note Added"}), 201


@note_bp.route('/', methods=['GET'])
@jwt_required()
def get_notes():
    user_id = get_jwt_identity()
    notes = Note.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": n.id, "content": n.content} for n in notes])


# ✅ NEW: Delete route for notes.html delete button
@note_bp.route('/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note(note_id):
    user_id = int(get_jwt_identity())
    note = Note.query.filter_by(id=note_id, user_id=user_id).first()
    if not note:
        return jsonify({"message": "Note not found"}), 404
    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": "Note deleted"}), 200
