import os

from models import User, Note
from flask import Flask
from extensions import db, bcrypt, jwt
from routes.auth_routes import auth_bp
from routes.note_routes import note_bp

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'notes.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['JWT_SECRET_KEY'] = 'secrecypeak'

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(note_bp, url_prefix='/notes')


@app.route('/')
def home():
    return {"message": "Welcome to Notes App!"}, 200


if __name__ == '__main__':
    app.run(debug=True)
