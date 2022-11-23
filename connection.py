import sqlalchemy as alchemy

class Db():
    def __init__(self):
        self.dialect = "mysql"
        self.username = "bella"
        self.password = "admin123"
        self.host = "localhost"
        # self.port = 
        self.database = "flaskdb"

        # dialect+driver://username:password@host:port/database

    def get_connection(self):
        engine = alchemy.create_engine("mysql+pymysql://{username}:{password}@{host}/{db}?charset=utf8&binary_prefix=true".format(
            username=self.username,
            password=self.password,
            host=self.host,
            db=self.database,
        ))

        connection = engine.connect()
        try:
            metadata = alchemy.MetaData()
            info = alchemy.Table('admins', metadata, autoload=True, autoload_with=engine)
            print(info.columns.keys())
            print("DB connected!!")
            return connection
        except Exception as e:
            print("Error connecting to database: ", e)


# db = Db()
# db.get_connection()
# engine =alchemy.create_engine("mysql+pymysql://bella:admin123@localhost/flaskdb")

