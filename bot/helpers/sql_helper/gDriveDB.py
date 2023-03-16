import pickle
import threading
from pymongo import MongoClient

client = MongoClient('mongodb://mongo:TpghbMFn6sO3JyPFzrRP@containers-us-west-148.railway.app:6601')
db = client['your_database_name']
collection = db['gDriveCreds']

INSERTION_LOCK = threading.RLock()

def _set(chat_id, credential_string):
    with INSERTION_LOCK:
        saved_cred = collection.find_one({'chat_id': chat_id})
        if not saved_cred:
            saved_cred = {'chat_id': chat_id}

        saved_cred['credential_string'] = pickle.dumps(credential_string)

        collection.save(saved_cred)


def search(chat_id):
    with INSERTION_LOCK:
        saved_cred = collection.find_one({'chat_id': chat_id})
        creds = None
        if saved_cred is not None:
            creds = pickle.loads(saved_cred['credential_string'])
        return creds


def _clear(chat_id):
    with INSERTION_LOCK:
        collection.delete_one({'chat_id': chat_id})
