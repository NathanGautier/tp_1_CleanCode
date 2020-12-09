# coding=utf-8
from flask import Flask
from flask_cors import CORS

from .config import config_by_name

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_by_name[config_name])
    return app
