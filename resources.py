from flask import Flask, request
from flask_restful import Resource, reqparse


app = Flask(__name__)

parser = reqparse.RequestParser()
parser.add_argument('numero', help='This field cannot be blank', required=True)

class Calculate(Resource):
    def get(self, num):

        num = num
        lista_divisores = []
        resultado = ''
        count = 0

        for i in range(1, num + 1):

            if num % i == 0:
                lista_divisores.append(i)
                count += 1

            if count == 2:
                resultado = (f'O número {num} é primo!')
            else:
                resultado = (f'O número {num} não é primo!')

        return (f"Divisores: {lista_divisores} Resultado: {resultado}")


