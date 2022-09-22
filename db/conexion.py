from pymongo import MongoClient

# Change the url_string if is neccesary with the follow format
# mongodb://[username:password@]host1[:port1]
DB_CONNECTION = 'mongodb://localhost:27017'

class Conexion():
  def __init__(self):
    self.client = MongoClient(DB_CONNECTION)
    self.db = self.client.squadMakers

  def create_database(self):
    try:
      dblist = self.client.list_database_names()
      if "squadMakers" in dblist:
        return "The database exists."
      else:
        db = self.client["squadMakers"]
        collection = db["joke"]
        collection.insert_one({
          "number": 1,
          "text": "joke example",
        })
        # collist = self.db.list_collection_names()
        return "The databases has been create"
    except Exception as e:
      print(type(e))
      raise "error creating database"
