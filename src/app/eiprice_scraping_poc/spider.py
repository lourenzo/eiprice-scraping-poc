import re

import requests
from bs4 import BeautifulSoup
import hjson

def parse_item_page(url):
    res = requests.get(url)
    html = res.content
    soup = BeautifulSoup(html, features='html.parser')
    data_script = soup.find(string = re.compile('digitalData ?='))
    adapted_script = re.sub( r'digitalData = ', '', data_script)
    adapted_script = re.sub( r';', '', adapted_script)
    parsed_object = hjson.loads(adapted_script)

    # Tip on how to extract EncodeURLComponent
    ''' re.sub(r'(?i)enc\((?:\"|\')([^\"\']+)(?:\"|\')\)', '\g<1>', 'enc("LALALa sadf asçãç ALALA")') '''
    return parsed_object


def extract_relevant_data(input):
    page = input.get('page')
    product = page.get('product')
    product_data = page.get('productData')
    best_installment_plan = product_data.get('seller').get('best_installment_plan')
    data = {
        'ean': product_data.get('variantions')[0].get('ean'),
        'sku': product.get('idSku'),
        'name': product.get('title')
    }
    return data
