from flask import Flask, request
from flask_restful import Resource, Api

import json

app = Flask(__name__)
api = Api(app)

# ARRAY EXEMPLE
receitas = [
{
    'title': "coxinha",
    'lista de ingredientes':[
        "frango",
        "catupiry",
        "massa",
        "fermento",
        "leite condensado"
    ],
    'modo de preparo': "leve ao forno por 10... depois ... e em seguida ...",
    'rendimento': "10 porções"
}
]

# GET ALL DATES
class Recs(Resource):
    def get(self):
        return {'status': 200, 'data': receitas}

    def post(self):
        newRec = json.loads(request.data)
        receitas.append(newRec)
        return {
            "message": "Updated!",
            "new": newRec
        }

# CRUD FUNCTIONS
class Rec(Resource):
    # GET OPTION
    def get(self, indice):
        try:
            return receitas[indice]
        except IndexError:
            message = "ID {} não encontrado!".format(indice)
            return {
                "mensage": message,
                "status": "Erro!"
            }
        except:
            message = "ID {} não encontrado!".format(indice)
            return {
                "mensage": message,
                "status": "Erro desconhecido!"
            }

    # PUT/UPDATE OPTION
    def put(self, indice):
        newValue = json.loads(request.data)
        receitas[indice] = newValue
        return {
            "message": "Updated!",
            "new": newValue
        }
    #DELETE OPTION
    def delete(self, indice):
        receitas.pop(indice)
        return {
            "message": "Removido!",
            "Lista de Receitas": receitas
        }


api.add_resource(Recs,'/recs/')
api.add_resource(Rec,'/recs/<int:indice>')

if __name__ == '__main__':
    app.run(debug=True)