FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN pip install --upgrade pip

COPY ./src/app /app
COPY ./src/app/requirements.txt /app

WORKDIR /app
RUN pip install -r requirements.txt
