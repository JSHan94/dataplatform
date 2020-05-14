var mysql = require('mysql');
var dbConfig = require('../config/database.js');
var con = mysql.createConnection(dbConfig);

exports.getDataInfo = (req,res) => {
  con.query('SELECT * from datainfo', function(err, rows) {
    if (err){
      throw err;
    }
    res.send(rows);
  });
};

exports.postData = (req,res) => {
  let data = req.body.data;
  con.query('INSERT INTO data (data) VALUES ' + "('"+data+"')", function(err, temp) {
    if (err){
      throw err;
    }
    res.sendStatus(200);
  })
};

exports.postDataInfo = (req,res) => {
  let name = req.body.name, category = req.body.category, price = req.body.price;
  let time;
  var sql = "INSERT INTO datainfo (name, category, price, time) VALUES ?";
  con.query('SELECT NOW()', function(err, dbTime) {
    if (err){
      throw err;
    }
    time = dbTime;
    var values = [[name, category, price, time]];
    con.query(sql, [values], function(err, temp) {
      if (err){
        throw err;
      }
      res.send(time);
    })
  });
};