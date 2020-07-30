FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN pip install pipenv
RUN pipenv install

COPY ./src/eiprice_scraping_poc /app
