import pymongo
import bottle
from bottle import route
from bottle import static_file
import sys
import json

import cgi
import string


@route('/')
def index():
  return static_file('login_form.html', root='./')


#handles a login request
@bottle.post('/login')
def process_login():
  username = bottle.request.json.get("username")
  password = bottle.request.json.get("password")

  print(bottle.request)

  print "user submitted ", username, "pass ", password


  #connnec to to the db on standard port
  connection = pymongo.MongoClient("mongodb://localhost")

  db = connection.test          # attach to db
  collection = db.users         # specify the collection

  try:
    item = collection.find_one({ "username": username, "password": password })
    print(str(item))
    # for item in iter:
    return json.dumps(str(item))
  except:
    print "Error trying to read collection:", sys.exc_info()[0]


bottle.run(host='localhost', port=8080)
