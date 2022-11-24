from flask import Flask
from flask_restful import Api, Resource

from views.view import viewInfo
from main import home
from connection import Db


app = Flask(__name__)

app.db = Db()
app.connection = app.db.get_connection()

api = Api(app)

app.add_url_rule('/', view_func=home)
api.add_resource(viewInfo, '/info')


if __name__ =="__main__":
    app.run(debug=True)
