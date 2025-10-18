import os
from dotenv import load_dotenv
from flask import Flask
from models import User, Note
from extensions import db, bcrypt, jwt
from routes.auth_routes import auth_bp
from routes.note_routes import note_bp
from flask import render_template, redirect, url_for

load_dotenv()


def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'instance', 'notes.db')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'secretkey')

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(note_bp, url_prefix='/notes')

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/notes')
    def notes_page():
        return render_template('notes.html')

    return app


if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', '5000'))
    app.run(host='0.0.0.0', port=port, debug=False)
