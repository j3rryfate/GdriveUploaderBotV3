from pymongo import MongoClient
from bot import DATABASE_URL, LOGGER

client = MongoClient(DATABASE_URL)
db = client[DRIVE_X]
parent_id = db["ParentID"]
gDrive = db['gDriveCreds']
