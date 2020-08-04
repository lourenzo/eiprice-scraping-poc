import re

import requests
from bs4 import BeautifulSoup
import hjson

'''
Obter urls de cada página da pesquisa de produtos
'''
def get_pages_list(url):
    res = requests.get(url)
    html = res.content
    soup = BeautifulSoup(html, features='html.parser')
    pagination_links = soup.find_all('li', class_='css-1a9p55p')
    pages_count = pagination_links.__len__() - 2
    page_urls = [url]

    for i in range(pages_count):
        if (i > 0):
            page_urls.append(url + '?page=' + str(i+1))

    return page_urls

'''
Obter URLs de produtos de todas as páginas da pesquisa
'''
def fetch_product_list(url):
    product_pages = get_pages_list(url)
    product_urls = []

    for page in product_pages:
        page_items = parse_list_page(page)
        product_urls += page_items

    return product_urls

'''
Obter urls de produtos de uma página específica da pesquisa
'''
def parse_list_page(url):
    res = requests.get(url)
    html = res.content
    soup = BeautifulSoup(html, features='html.parser')
    product_urls = []

    # Obter itens desta página
    for link in soup.find_all('a', {'name': 'linkToProduct'}):
        product_urls.append(link.get('href'))

    return product_urls

'''
Extrair dados da página de um produto
'''
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
    parsed_object['url'] = url
    return extract_relevant_data(parsed_object)

'''
Extrair dados relevantes dos dados brutos de um produto
'''
def extract_relevant_data(input_data):
    page = input_data['page']
    product = page['product']
    product_data = page['productData']
    best_installment_plan = product_data['seller']['best_installment_plan']
    main_variation = product_data['variantions'][0]
    category = main_variation['categories'][0]

    data = {
        'ean': product_data['variantions'][0]['ean'],
        'sku': product['idSku'],
        'name': product['title'],
        'department': category['name'],
        'category': category['subcategories'][1]['name'],
        'subcategory': category['subcategories'][0]['name'],
        'brand': product['brand'],
        'attributes': main_variation['attributes'],
        'in_stock': product['stockAvailability'],
        'price': product['salePrice'],
        'installments': best_installment_plan['installment_quantity'],
        'installment_price': best_installment_plan['installment_amount'],
        'interest_rate': best_installment_plan['interest'],
        'url': input_data['url'],
        'image': product['imageUrl']
    }
    return data
