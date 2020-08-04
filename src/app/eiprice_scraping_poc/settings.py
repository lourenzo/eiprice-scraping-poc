from dotenv import load_dotenv
load_dotenv()
from os import environ as env

def plain_val(x):
    return x

def optional_setting(app, key, serializer=plain_val):
    if env.keys().__contains__(key):
        app.config[key] = serializer(env[key])

def load_settings(app):
    app.config['MONGODB_DB'] = env['MONGODB_DB']
    optional_setting(app, 'MONGODB_HOST')
    optional_setting(app, 'MONGODB_PORT', serializer=int)
    optional_setting(app, 'MONGODB_USERNAME')
    optional_setting(app, 'MONGODB_PASSWORD')
