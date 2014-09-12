var express = require('express');
var mongoose = require('mongoose');


var UserSchema = new mongoose.Schema({
  nickname: String,
  username: String,
  password: String
});

var Users = mongoose.model('users', UserSchema);

var app = express();

app.use(require('body-parser').urlencoded({extended: true}));


app.get('/', function(req, res) {
  res.render('login_form.html', {});
});


app.post('/', function(req, res) {
  Users.findOne({user: req.body.user, pass: req.body.pass}, function (err, user) {
    if (err) {
      return res.status(500).send({message: err.message});
    }

    if (!user) {
      return res.status(500).send({message: 'Sorry!'});
    }

    return res.status(200).send({ message: 'Welcome back ' + user.name + '!!!'});
  });
});



var server = app.listen(49090, function () {
  mongoose.connect('mongodb://localhost/test');
  console.log('listening on port %d', server.address().port);
});