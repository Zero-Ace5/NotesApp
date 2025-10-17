from flask import Blueprint, request, jsonify
from app import db
from models import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    return 1


@auth_bp.route('/login', methods=['POST'])
def login():
    return 1
