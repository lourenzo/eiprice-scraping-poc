from flask import Flask

from .settings import load_settings
from .models import db
from .routes import create_routes
from .commands import add_custom_commands

''' Application Factory '''
def create_app():
    app = Flask(__name__)

    load_settings(app)
    db.init_app(app)
    add_custom_commands(app)
    create_routes(app)

    return app
