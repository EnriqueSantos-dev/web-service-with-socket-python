FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH /usr/app

EXPOSE ${SERVER_PORT}

CMD [ "python", "src/app.py" ]


