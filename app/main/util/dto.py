from flask_restx import Namespace, fields

class ClientDto:
    api = Namespace('client', description='client related operations')
    client = api.model('client', {
        'id': fields.String(required=True, description='Client identifier')
    })