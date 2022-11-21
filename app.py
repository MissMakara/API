from flask import Flask
from flask_restful import Api, Resource

from view import viewInfo
from main import home


app = Flask(__name__)
api = Api(app)

app.add_url_rule('/', view_func=home)
api.add_resource(viewInfo, '/info')

if __name__ =="__main__":
    app.run(debug=True)
