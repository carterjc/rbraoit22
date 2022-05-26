FROM python:3.9.12-alpine3.15

COPY ./requirements.txt /

RUN pip3 install -r /requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT [ "./guicorn_starter.sh" ]
