const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://deishacks:<PASSWORD>@waltham-tlvvt.gcp.mongodb.net/test?retryWrites=true";
const client = new MongoClient(uri, { useNewUrlParser: true });
client.connect(err => {
  const collection = client.db("test").collection("names");
 // perform actions on the collection object
  client.close();
});
