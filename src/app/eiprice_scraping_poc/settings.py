from dotenv import load_dotenv
load_dotenv()
from os import environ as env

def load_settings(app):
    app.config['MONGODB_DB'] = env['MONGODB_DB']
    app.config['MONGODB_HOST'] = env['MONGODB_HOST']
    app.config['MONGODB_PORT'] = int(env['MONGODB_PORT'])
    app.config['MONGODB_USERNAME'] = env['MONGODB_USERNAME']
    app.config['MONGODB_PASSWORD'] = env['MONGODB_PASSWORD']
