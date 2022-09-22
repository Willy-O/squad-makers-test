from db.conexion import Conexion

class Joke(Conexion):

  def get_all(self):
    try:
      data = self.db.joke.find({}, {'_id': 0})
      return list(data) 
    except Exception as e:
      print(e)
      raise

  def get_one(self):
    try:
      data = self.db.joke.find({}, {'_id': 0})
      return list(data) 
    except Exception as e:
      print(e)
      raise


  def insert_one(self, data):
    try:
      lastNumber = self.db.joke.find().sort([('number', -1)]).limit(1)
      num = list(lastNumber)[0]['number']
      data['number'] = int(num) + 1
      self.db.joke.insert_one(data)
      return True
    except Exception as e:
      print(e)
      raise

  def update_one(self, text, number):
    try:
      self.db.joke.update_one({
        'number': number
      },{
        '$set':{
          'text': text
        }
      })
      return True
    except Exception as e:
      print(e)
      raise

  def delete_one(self, id):
    try:
      a= self.db.joke.delete_one({'number': id})
      return True
    except Exception as e:
      print(e)
      raise
