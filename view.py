from flask_restful import Resource, Api
from flask import request, current_app

class viewInfo(Resource):
    def __init__(self):
        pass

    def get(self):
        return "You can view the info page!!"

    def post(self):
        payload = request.get_json()
        response = self.display(payload)
        return response

    def display(self, info):
        return info


