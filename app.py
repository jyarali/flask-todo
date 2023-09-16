from flask import Flask
from db import db
import models


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"
    return app
