import pymongo
URL = "mongodb+srv://deishacks:louisbrandeis@waltham-tlvvt.gcp.mongodb.net/test?retryWrites=true"

client = pymongo.MongoClient(URL)
connect = client.test
db = client["test"]

post_col = db["posts"]
route_col = db["routes"]
ride_col = db["rides"]

#print(db.list_collection_names())
#print(db.command("serverStatus"))


class post:

    def __init__(self, content, street, city, state, zip, long, lat, main_category, tags,
        timestamp, upvotes, active_status):

        self.content = content
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.long = long
        self.lat = lat
        self.main_category = main_category
        self.tags = tags
        self.timestamp = timestamp
        self.upvotes = upvotes
        self.active_status = active_status

class route:

    def __init__ (self, origin_street, origin_city, origin_state, origin_zip,
        origin_long, origin_lat, dest_street, dest_city, dest_state, dest_zip,
        dest_long, dest_lat, image_URL, comment):

        self.origin_street = origin_street
        self.origin_city = origin_city
        self.origin_state = origin_state
        self.origin_zip = origin_zip
        self.origin_long = origin_long
        self.origin_lat = origin_lat
        self.dest_street = dest_street
        self.dest_city = dest_city
        self.dest_state = dest_state
        self.dest_zip = dest_zip
        self.dest_long = dest_long
        self.dest_lat = dest_lat
        self.image_URL = image_URL
        self.comment = comment

class ride:

    def __init__(self, content, street, city, state, zip, long, lat, timestamp,
        active_status, user_email):

        self.content = content
        self.user_email = user_email
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.long = long
        self.lat = lat
        self.timestamp = timestamp
        self.active_status = active_status
