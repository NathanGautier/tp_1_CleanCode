
FROM python:3.8.2

WORKDIR /app

ADD . /app

ENV UFO_ENV 'prod'

RUN pip install -r requirements.txt

RUN python manage.py db upgrade

RUN python manage.py import_data

EXPOSE 5000

CMD ["python", "./manage.py", "run"]
