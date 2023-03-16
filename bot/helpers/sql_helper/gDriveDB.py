import pickle
import threading
from pymongo import MongoClient

client = MongoClient('mongodb://mongo:TpghbMFn6sO3JyPFzrRP@containers-us-west-148.railway.app:6601')
db = client['your_database_name']
collection = db['gDriveCreds']

INSERTION_LOCK = threading.RLock()

def _set(chat_id, credential_string):
    with INSERTION_LOCK:
        filter_query = {'chat_id': chat_id}
        credential_string_pickle = pickle.dumps(credential_string)
        update_query = {'$set': {'credential_string': credential_string_pickle}}
        collection.update_one(filter_query, update_query, upsert=True)


def search(chat_id):
    with INSERTION_LOCK:
        saved_cred = collection.find_one({'chat_id': chat_id})
        creds = None
        if saved_cred is not None:
            credential_string_pickle = saved_cred['credential_string']
            creds = pickle.loads(credential_string_pickle)
        return creds


def _clear(chat_id):
    with INSERTION_LOCK:
        collection.delete_one({'chat_id': chat_id})
