import databases
import sqlalchemy

DATABASE_URL = "mysql://localhost/example"

Database = databases.Database(DATABASE_URL)
Engine = sqlalchemy.create_engine(str(Database.url))