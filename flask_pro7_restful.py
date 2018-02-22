from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class IndexView(Resource):
    def get(self):
        return {"username": "zhiliao"}


api.add_resource(IndexView, '/', endpoint='index')

if __name__ == '__main__':
    app.run(debug=True, port=5007)
