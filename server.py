import pymongo
from bson.json_util import dumps
import bottle
from bottle import response
from bottle import route
from bottle import static_file
import sys



@route('/')
def index():
  # return static_file('login_form.html', root='./')
  return open('login_form.html').read()


#handles a login request
@bottle.post('/login')
def post_login():
  response.content_type = 'application/json'
  username = bottle.request.json.get("username")
  password = bottle.request.json.get("password")

  print "user submitted ", username, "pass ", password


  #connnec to to the db on standard port
  connection = pymongo.MongoClient("mongodb://localhost")

  db = connection.test          # attach to db
  collection = db.users         # specify the collection

  try:
    item = collection.find_one({ "username": username, "password": password })
    print(str(item))
    return dumps(item)
  except:
    print "Error trying to read collection:", sys.exc_info()[0]
    return { 'message': sys.exc_info()[0] }


# http://localhost:8080/login?username=name1&password=pass1
# http://localhost:8080/login?username[$gt]=&password[$gt]=
# @bottle.get('/login')
# def get_login():
#   username = bottle.request.query.getall("username")
#   password = bottle.request.query.password

#   print "user submitted ", username, "pass ", password


#   #connnec to to the db on standard port
#   connection = pymongo.MongoClient("mongodb://localhost")

#   db = connection.test          # attach to db
#   collection = db.users         # specify the collection

#   try:
#     item = collection.find_one({ "username": username, "password": password })
#     print(str(item))
#     return dumps(item)
#   except:
#     print "Error trying to read collection:", sys.exc_info()[0]
#     return { 'message': sys.exc_info()[0] }

bottle.run(host='localhost', port=8080)
