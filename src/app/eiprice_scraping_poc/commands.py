import sys

import click
import json

from .models import ProductOffer

from .spider import parse_item_page, fetch_product_list

def add_custom_commands(app):
    @app.cli.command('fetch_data')
    def fetch_data():
        print('Fetch data from page', file=sys.stderr)
        product_urls = fetch_product_list(
            'https://www.magazineluiza.com.br/aquecedor-eletrico/ar-e-ventilacao/s/ar/arae/brand---mondial'
        )
        for url in product_urls:
            productData = parse_item_page(url)
            #print(productData)
            ProductOffer(**productData).save()

    @app.cli.command('fetch_list')
    def fetch_list():
        print('Fetch items from listing page', file=sys.stderr)
        url = 'https://www.magazineluiza.com.br/aquecedor-eletrico/ar-e-ventilacao/s/ar/arae/brand---mondial/'
        data = fetch_product_list(url)
        print(json.dumps(data, indent=2))

