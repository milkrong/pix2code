import werkzeug
from flask_restful import Resource, reqparse

from app.model import sample


class DslResource(Resource):
    def get(self):
        return 'hello'
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('screen_shot',
                            required=True,
                            help="File must not be empty",
                            type=werkzeug.datastructures.FileStorage,
                            location='files')
        args = parser.parse_args()
        file = args['screen_shot']
        print(args)
        if not file:
            return 'Invalid file'
        dsl = sample.sample_image(file)
        return dsl
