from models import User, Note
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp
from routes.note_routes import note_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/notes.db'
app.config['JWT_SECRET_KEY'] = 'secrecypeak'

db = SQLAlchemy(app)


with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(note_bp, url_prefix='/notes')


@app.route('/')
def home():
    return {"message": "Welcome to Notes App!"}, 200


if __name__ == '__main__':
    app.run(debug=True)
