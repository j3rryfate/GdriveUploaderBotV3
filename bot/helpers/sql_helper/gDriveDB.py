import pickle
import threading
from pymongo import MongoClient
from bson.binary import Binary

# Create a MongoClient instance to connect to the MongoDB instance
client = MongoClient('mongodb://mongo:TpghbMFn6sO3JyPFzrRP@containers-us-west-148.railway.app:6601/')

# Select the database and collection to use
db = client['Drive_X']
collection = db['gDrive']

class gDriveCreds:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.credential_string = None

    def to_dict(self):
        return {'chat_id': self.chat_id, 'credential_string': self.credential_string}

    def from_dict(self, data):
        self.chat_id = data['chat_id']
        self.credential_string = data['credential_string']

def _set(chat_id, credential_string):
    # Create a new gDriveCreds object with the given chat_id and credential_string
    creds = gDriveCreds(chat_id)
    creds.credential_string = Binary(pickle.dumps(credential_string))

    # Insert or update the document in the collection
    collection.replace_one({'chat_id': chat_id}, creds.to_dict(), upsert=True)

def search(chat_id):
    # Find the document with the given chat_id in the collection
    result = collection.find_one({'chat_id': chat_id})
    if result is not None:
        # If a document was found, create a new gDriveCreds object from the data
        creds = gDriveCreds(None)
        creds.from_dict(result)
        creds.credential_string = pickle.loads(result['credential_string'])
        return creds
    else:
        return None

def _clear(chat_id):
    # Delete the document with the given chat_id from the collection
    collection.delete_one({'chat_id': chat_id})
