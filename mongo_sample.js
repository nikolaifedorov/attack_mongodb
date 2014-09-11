var dbName = "test";
var collectionName = "users";


function initialize(){
    
	var db2 = db.getSiblingDB(dbName);
    
	var collection = db2[collectionName];
    
	collection.drop();

    
	collection.insert({ username: "name1", password: "pass1" });
	collection.insert({ username: "name2", password: "pass2" });
  collection.insert({ username: "name3", password: "pass3" });
  collection.insert({ username: "name4", password: "pass4" });
  collection.insert({ username: "name5", password: "pass5" });
}


function find() {
	return db.users.find()
}


function injection_query(req) {
	return db.users.find({username: req.body.username, password: req.body.password})
}


function obj_to_srt_query(req) {
	return db.users.find({ username: (req.body.username || "").toString(10), password: (req.body.password || "").toString(10) })
}


function query_with_explicity_qs(req) {
	return db.users.find({ username: { $in: [req.body.username] }, password: { $in: [req.body.password] } })
}


function find_data(username, password) {
	//print("db.users.find({username:" +  username + ", password: " + password + "})")
	return db.users.find({username: username, password: password})
}


function getQSReq() {
	var req = { 
		body: {
			username: { "$gt": "" },
			password: { "$gt": "" }
		}
	};
	
	return req;
}


function getValidReq() {
	var req = { 
		body: {
			username: "name2",
			password: "pass2"
		}
	};
	
	return req;
}

function getStrSQLI() {
 return "{ $ne: '' } }) //"
}
// find_data("\{ $ne: ''\}\}\)//", "pass1")
