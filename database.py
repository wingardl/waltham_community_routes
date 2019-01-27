import pymongo
import datetime
import gridfs
import os

# Constants
URL = "mongodb+srv://deishacks:louisbrandeis@waltham-tlvvt.gcp.mongodb.net/test?retryWrites=true"
TIMESTAMP = datetime.datetime.now()

client = pymongo.MongoClient(URL)
connect = client.test
db = client["test"]
fs = gridfs.GridFS(db)

post_col = db["posts"]
route_col = db["routes"]
ride_col = db["rides"]

#print(db.list_collection_names())
#print(db.command("serverStatus"))


class Post:

    def __init__(self, content, street, city, state, zip, long, lat, main_category, tags,
        timestamp, upvotes, active):

        self.dict = {"content": content, "street": street, "city": city,
            "state": state, "zip": zip, "long": long, "lat": lat,
            "main_category": main_category, "tags": tags, "timestamp": timestamp,
            "upvotes": upvotes, "active": active}

    def push(self):

        post_id = post_col.insert_one(self.dict)

    def get(self):

        return self.dict

class Route:

    def __init__ (self, origin_street, origin_city, origin_state, origin_zip,
        origin_long, origin_lat, dest_street, dest_city, dest_state, dest_zip,
        dest_long, dest_lat, image_URL, comment):

        image_id = fs.put(open(image_URL, 'rb'))

        self.dict = {"origin_street": origin_street, "origin_city": origin_city,
            "origin_state": origin_state, "origin_zip": origin_zip, "origin_long": origin_long,
            "origin_lat": origin_lat, "dest_street": dest_street, "dest_city": dest_city,
            "dest_state": dest_state, "dest_zip": dest_zip, "dest_long": dest_long,
            "dest_lat": dest_lat, "image_id": image_id, "comment": comment}

    def push(self):

        route_id = route_col.insert_one(self.dict)

    def get(self):
        return self.dict


class Ride:

    def __init__(self, content, street, city, state, zip, long, lat, timestamp,
        active, user_email):

        self.dict = {"content": content, "user_email": user_email, "street": street,
        "city": city, "state": state, "zip": zip, "long": long, "lat": lat,
        "timestamp": timestamp, "active": active}

    def push(self):

        ride_id = ride_col.insert_one(self.dict)

    def get(self):
        return self.dict


def fetch_posts(query='None'):
    posts = []
    if query == 'None':
        for post in post_col.find():
                posts.append(post)
    else:
        for post in post_col.find(query):
                posts.append(post)
    return posts

def fetch_routes(query='None'):
    routes = []
    if query == 'None':
        for route in route_col.find():
                routes.append(route)
    else:
        for route in route_col.find(query):
                routes.append(route)
    return routes

def fetch_rides(query='None'):
    rides = []
    if query == 'None':
        for ride in ride_col.find():
                rides.append(ride)
    else:
        for ride in ride_col.find(query):
                rides.append(ride)
    return rides

def fetch_image(image_id):
    return fs.find(image_id)


if __name__ == "__main__":

    test_post = Post("first post test", "South Street", "Waltham", "MA", "02453",
        "71.25798773655532", "42.3663164", "Road Blockage", "construction",
        TIMESTAMP, 0, True)

    test_route = Route("South Street", "Waltham", "MA", "02453", "71.25798773655532",
        "42.3663164", "Moody Street","Waltham", "MA", "02453", "71.237476400", "42.367904200",
        "brandeis-sign.jpg", "first route test")

    test_ride = Ride("first ride test", "South Street", "Waltham", "MA", "02453", "71.25798773655532",
        "42.3663164", TIMESTAMP, True, "user@brandeis.edu")


    #test_post.push()
    #test_ride.push()
    test_route.push()

    for route in route_col.find({},{"image_id": 1}):
       fetch_image(route["image_id"])

    #post_col.delete_many({})
    #route_col.delete_many({})
    #ride_col.delete_many({})

    #print(fetch_posts())
    #print(fetch_routes())
    #print(fetch_rides())


    #print(fetch_posts({"active": True}))
    #print(fetch_routes())
    #print(fetch_rides({"active": False}))
