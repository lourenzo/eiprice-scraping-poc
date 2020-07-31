from flask import Flask

from .settings import load_settings
from .models import db
from .routes import create_routes

''' Application Factory '''
def create_app():
    app = Flask(__name__)

    load_settings(app)
    db.init_app(app)
    create_routes(app)

    return app
