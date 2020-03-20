from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

import resources, views

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,HEAD,OPTIONS,POST,PUT')
    response.headers.add('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization')
    return response


api.add_resource(resources.Calculate, '/calculate/<int:num>')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)), host='0.0.0.0')