from pymongo import MongoClient

# Set up the MongoDB connection
client = MongoClient('mongodb://localhost:27017/')

# Access a database
db = client['Drive_']

# Access a collection within the database
collection = db['gDriveDB']
collection1 = db['ParentID']
