var MongoClient = require('mongodb').MongoClient;
  var url = "mongodb+srv://deishacks:louisbrandeis@waltham-tlvvt.gcp.mongodb.net/test?retryWrites=true";

  MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("test");
    dbo.collection("names").find({}).toArray(function(err, result) {
      if (err) throw err;
      console.log(result);
      db.close();
    });
  });
