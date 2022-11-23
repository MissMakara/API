from flask_restful import Resource, Api
from flask import request, current_app
from sqlalchemy.sql import text as sql_text
import uuid



class viewInfo(Resource):
    def __init__(self):
        self.connection = current_app.connection

    def get(self):
        print("You can view the info page!!")
        response = self.dbFetch()
        return response

    def post(self):
        payload = request.get_json()

        response = self.dbInsert(payload)
        return response

    def dbInsert(self, info):
        print("Inserting into db")
        try:
            uuid_val = str(uuid.uuid4())
            print("uuid value is {}".format(uuid_val))

            #iterate through the info list and put the items into a dictionary
            for element in info:
                data ={
                    "uuid": uuid_val,
                    "firstname":element["first_name"],
                    "lastname":element["last_name"]
                }

            query = "insert into admins( admin_id, first_name, last_name) values (UUID_TO_BIN(:uuid), :firstname, :lastname)"
            result = self.connection.execute(sql_text(query), data)
            print("result received", result)
            return "success"

        except Exception as e:
            print("Could not insert the data due to error: ", e)

    def dbFetch(self):            
        query = "select * from admins"
        ResultProxy = self.connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        
        return ResultSet



# id=my_conn.execute("INSERT INTO  `database_name`.`student` (`name` ,`class` ,`mark` ,`sex`) \
#                   VALUES ('King1',  'Five',  '45',  'male')")