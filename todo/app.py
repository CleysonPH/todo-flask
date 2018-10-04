from flask import Flask

import views
import db


def create_app():
    app = Flask(__name__)

    views.configure(app)

    db.configure(app)

    return app
