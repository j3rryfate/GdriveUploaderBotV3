from pymongo import MongoClient

# Set up the MongoDB connection
client = MongoClient('mongodb://mongo:TpghbMFn6sO3JyPFzrRP@containers-us-west-148.railway.app:6601')

# Access a database
db = client['Drive_']

# Access a collection within the database
collection = db['gDriveDB']
collection1 = db['ParentID']
