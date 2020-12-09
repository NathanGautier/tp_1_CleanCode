from flask import request
from flask_restx import Resource
from ..util.dto import ClientDto
from ..service.client_service import is_int, verify_id, response_object

api = ClientDto.api # import our DTO (api namespace) This namespace is also providing decorators (annotations)
_client = ClientDto.client # import our DTO (api model for marshaling)

@api.route('/cle/verification/<client_id>')
@api.param('client_id', 'The Client identifier')
@api.response(404, 'Client not found.')
class User(Resource):
    @api.doc('to authenticate')
    @api.marshal_with(_client)
    def get(self, client_id):
        """verify if the identifier is correct"""

        # controle saisie string + longeur <= 9
        if(len(client_id) == 10 and type(client_id) == str):

            # on sépare la lettre des chiffres
            key = client_id[:2].upper()
            identifier = client_id[1:]
            if is_int(identifier):
                # on regarde si la cle correspond a l'identifiant 
                return verify_id(key, identifier)
            else:
                #api.abort(404)            
                return response_object('failed', client_id, 0)
        