FROM python:3.10

RUN pip install pipenv

WORKDIR /code/

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

COPY . /code/

EXPOSE 8000