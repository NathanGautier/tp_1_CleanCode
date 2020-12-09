from flask_restx import Api
from flask import Blueprint

from .main.controller.client_controller import api as client_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='UFO API',
          version='1.0',
          description='a well designed Flask API ...',
          security='Bearer Auth'
          )

api.add_namespace(client_ns, path='/client')
