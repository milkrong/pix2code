import os

from flask import Flask

from flask_restful import Api

import service.dsl

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():

    app = Flask(__name__)
    api_instance = Api(app)
    api_instance.add_resource(service.dsl.DslResource, '/', '/generate_dsl')

    app.run(debug=True)


if __name__ == '__main__':
    main()
