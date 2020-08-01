import sys

import click
import json

from .spider import parse_item_page

def add_custom_commands(app):
    @app.cli.command('fetch_data')
    def fetch_data():
        print("Fetch data from page", file=sys.stderr)
        url = 'https://www.magazineluiza.com.br/aquecedor-halogeno-mondial-comfort-air-a-09-8970-02-220v/p/eh7962327j/ar/arae/'
        data = parse_item_page(url)
        print(json.dumps(data, indent=2))
