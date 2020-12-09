from flask import request
from flask_restx import Resource
from ..util.dto import ClientDto
from ..service.client_service import is_int, verify_id, response_object, creation_id


# import our DTO (api namespace) This namespace
# is also providing decorators (annotations)
api = ClientDto.api


@api.route('/cle/verification')
@api.doc(params={'id': 'The client identifier'}, location='query')
class Client(Resource):
    @api.doc('ID integrity check')
    def get(self):
        client_id = str(request.args.get('id', 1))

        if(len(client_id) == 10 and type(client_id) == str):

            # on sépare la lettre des chiffres
            key = client_id[0].upper()
            identifier = client_id[1:]
            if is_int(identifier):
                # on regarde si la cle correspond a l'identifiant
                return verify_id(key, identifier)
            else:
                return response_object('failed', client_id, 0)

        else:
            return response_object('failed', client_id, 0)


@api.route('/cle/creation')
@api.doc(params={'id': 'Give me an integer'}, location='query')
class Creation(Resource):
    @api.doc('ID integrity check')
    def get(self):
        id = str(request.args.get('id', 1))

        return creation_id(id)
