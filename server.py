import pymongo
import bottle
import sys
import cgi
import string



#handles a login request
@bottle.post('/login')
def process_login():
  username = bottle.request.forms.get("username")
  password = bottle.request.forms.get("password")
  
  print "user submitted ", username, "pass ", password


  #connnec to to the db on standard port
  connection = pymongo.MongoClient("mongodb://localhost")

  db = connection.test          # attach to db
  collection = db.users         # specify the collection

  try:
    iter = collection.find({})
    for item in iter:
      return str(item) + "\n"
  except:
    print "Error trying to read collection:", sys.exc_info()[0]


bottle.run(host='localhost', port=8080)
