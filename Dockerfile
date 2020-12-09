
FROM python:3.8.2

WORKDIR /app

ADD . /app

ENV UFO_ENV 'prod'

RUN pip install -r requirements.txt

RUN python manage.py db upgrade

EXPOSE 5000

CMD ["python", "./manage.py", "run"]
