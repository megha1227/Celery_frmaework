from flask import Flask
from flask_restful import Resource,Api

from task import task

app = Flask(__name__)
api = Api(app)

class Testing(Resource):
    def get(self):
        task.delay()
        return "Hello World"

api.add_resource(Testing,'/')


if __name__ == "__main__":
    app.run(debug=True)