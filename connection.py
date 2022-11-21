import sqlalchemy as alchemy

# class Db:
#     def __init__(self):
#         self.dialect = mysql
#         self.username = bella
#         self.password = admin123
#         self.host = localhost
#         # self.port = 
#         self.database = flaskdb

#         # dialect+driver://username:password@host:port/database


engine =alchemy.create_engine("mysql+pymysql://bella:admin123@localhost/flaskdb")
connection = engine.connect()
metadata = alchemy.MetaData()
info = alchemy.Table('admins', metadata, autoload=True, autoload_with=engine)
print(info.columns.keys())

