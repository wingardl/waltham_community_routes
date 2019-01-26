from pymongo import MongoClient
client = MongoClient("mongodb+srv://deishacks:louisbrandeis@waltham-tlvvt.gcp.mongodb.net/test?retryWrites=true")
db = client.test
