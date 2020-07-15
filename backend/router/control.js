var mysql = require('mysql');
var dbConfig = require('../config/database.js');
var con = mysql.createConnection(dbConfig);

exports.getData = (req,res) => {
  let datahash = req.query.datahash;
  con.query('SELECT * from db WHERE datahash = "' + datahash + '"', function(err, respond) {
    if (err){
      throw err;
    }
    if(respond[0] == null){
      res.send("error");
    }
    else{
      res.send(respond[0].decrypt);
    }
  });
};

exports.getDataInfo = (req,res) => {
  con.query('SELECT * from datainfo WHERE state = 0', function(err, rows) {
    if (err){
      throw err;
    }
    res.send(rows);
  });
};

exports.getUserInfo = (req,res) => {
  con.query('SELECT * from balanceinfo', function(err, rows) {
    if (err){
      throw err;
    }
    res.send(rows);
  });
};

exports.getUserBalance = (req,res) => {
  let user = req.query.user;
  con.query('SELECT * from balanceinfo WHERE user = "' + user + '"', function(err, respond) {
    if (err){
      throw err;
    }
    if(respond[0]==undefined)
      res.send('0')
    else
      res.send(respond[0].balance.toString());
  });
};

exports.getUserDataInfo = (req,res) => {
  let user = req.query.user;
  con.query('SELECT * from datainfo WHERE buyer = "' + user + '"', function(err, rows) {
    if (err){
      throw err;
    }
    res.send(rows);
  });
};

exports.postData = (req,res) => {
  let data = req.body.data;
  var sql = "INSERT INTO db (decrypt) VALUES ?";
  var values = [[data]];
  con.query(sql, [values], function(err, temp) {
    if (err){
      throw err;
    }
    res.sendStatus(200);
  })
};

exports.postDataInfo = (req,res) => {
  let name = req.body.name, category = req.body.category, price = req.body.price, owner = req.body.owner;
  let datahash = 3;
  var sql = "INSERT INTO datainfo (name, category, price, owner, datahash) VALUES ?";
  var values = [[name, category, price, owner, datahash]];
  con.query(sql, [values], function(err, temp) {
    if (err){
      throw err;
    }
    res.sendStatus(200);
  })
};