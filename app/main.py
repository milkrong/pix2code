from flask import Flask

from flask_restful import Api
from app.service.dsl import DslResource
from app.model_generator import load_model

def run_app():

    app = Flask(__name__)
    api_instance = Api(app)
    api_instance.add_resource(DslResource, '/', '/generate_dsl')
    print('load model')
    load_model()
    app.run(debug=True)
  
