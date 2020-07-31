from flask import jsonify

def create_routes(app):

    ''' TODO: serve app docs at / '''
    @app.route('/')
    def hello():
        return jsonify({
            'api': 'eiprice-scraping-poc',
        })
