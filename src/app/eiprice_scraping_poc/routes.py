from flask import jsonify
from flask_api import FlaskAPI, status, exceptions

from .models import ProductOffer

def create_routes(app):

    ''' TODO: serve app docs at / '''
    @app.route('/')
    def hello():
        return jsonify({
            'api': 'eiprice-scraping-poc',
            'routes': [
                {
                    'path': '/product-offers/by/ean/<ean>',
                    'description': 'Consulta por ean'
                },
                {
                    'path': '/product-offers/by/sku/<sku>',
                    'description': 'Consulta por sku'
                },
                {
                    'path': '/product-offers/availability',
                    'description': 'Relatório Quantidade de produtos disponíveis / ruptura'
                },
                {
                    'path': '/product-offers/market-share',
                    'description': 'Relatório de Market share'
                },
            ]
        })


    ''' Consulta por ean '''
    @app.route('/product-offers/by/ean/<ean>')
    def list_product_offers_by_ean(ean):
        items = ProductOffer.objects(ean=ean)
        if items.__len__() > 0:
            return items[0]
        else:
            raise exceptions.NotFound()


    ''' Consulta por sku '''
    @app.route('/product-offers/by/sku/<sku>')
    def list_product_offers_by_sku(sku):
        items = ProductOffer.objects(sku=sku)
        if items.__len__() > 0:
            return items[0]
        else:
            raise exceptions.NotFound()

    ''' Relatório Quantidade de produtos disponíveis / ruptura '''
    @app.route('/product-offers/availability')
    def availability_report():
        available_count = ProductOffer.objects(in_stock=True).count()
        unavailable_count = ProductOffer.objects(in_stock=False).count()
        return { 'available': available_count, 'unavailable': unavailable_count }


    ''' Relatório de Market share '''
    @app.route('/product-offers/market-share')
    def market_share_report():
        total_count = ProductOffer.objects.count()
        return { 'market-share': total_count }
