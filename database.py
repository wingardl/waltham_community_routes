import pymongo
import datetime

# Constants
URL = "mongodb+srv://deishacks:louisbrandeis@waltham-tlvvt.gcp.mongodb.net/test?retryWrites=true"
TIMESTAMP = datetime.datetime.now()

client = pymongo.MongoClient(URL)
connect = client.test
db = client["test"]

post_col = db["posts"]
route_col = db["routes"]
ride_col = db["rides"]

#print(db.list_collection_names())
#print(db.command("serverStatus"))


class Post:

    def __init__(self, content, street, city, state, zip, long, lat, main_category, tags,
        timestamp, upvotes, active):

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
        self.active = active

    def push(self):

        post_dict = {"content": self.content, "street": self.street, "city": self.city,
            "state": self.state, "zip": self.zip, "long": self.long, "lat": self.lat,
            "main_category": self.main_category, "tags": self.tags, "timestamp": self.timestamp,
            "upvotes": self.upvotes, "active": self.active}

        post_id = post_col.insert_one(post_dict)

class Route:

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

    def push(self):

        route_dict = {"origin_street": origin_street, "origin_city": origin_city,
            "origin_state": origin_state, "origin_zip": origin_zip, "origin_long": origin_long,
            "origin_lat": origin_lat, "dest_street": dest_street, "dest_city": dest_city,
            "dest_state": dest_state, "dest_zip": dest_zip, "dest_long": dest_long,
            "dest_lat": dest_lat, "image_URL": image_URL, "comment": comment}

        route_id = route_col.insert_one(route_dict)

class Ride:

    def __init__(self, content, street, city, state, zip, long, lat, timestamp,
        active, user_email):

        self.content = content
        self.user_email = user_email
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.long = long
        self.lat = lat
        self.timestamp = timestamp
        self.active = active

    def push(self):

        ride_dict = {"content": self.content, "user_email": user_email, "street": self.street,
        "city": self.city, "state": self.state, "zip": self.zip, "long": self.long, "lat": self.lat,
        "timestamp": self.timestamp, "active": self.active}

        ride_id = ride_col.insert_one(ride_dict)


if __name__ == "__main__":

    test_post = Post("first post test", "South Street", "Waltham", "MA", "02453",
        "71.25798773655532", "42.3663164", "Road Blockage", "construction",
        TIMESTAMP, 0, True)

    #test_post.push()

    #for post in post_col.find():
    #    print(post)
