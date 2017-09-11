from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class CreateSession(Resource):
  def post(self):
    return '{"id": 1}', 201

class EndSession(Resource):
  def delete(self, session_id):
    return '', 204

api.add_resource(CreateSession, '/session')
api.add_resource(EndSession, '/session/<session_id>')

if __name__ == '__main__':
  app.run(port=5002)
