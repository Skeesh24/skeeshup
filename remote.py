from typing import Dict
from urllib.parse import quote_plus

from pymongo import MongoClient

from settings import env

URI = "mongodb+srv://%s:%s@%s" % (
    quote_plus(env.MONGO_USER),
    quote_plus(env.MONGO_PASSWORD),
    env.MONGO_HOST,
)

def get_remote_configuration() -> Dict:
    collection = collection_connect()
    conf = collection.find_one()
    if conf is None or conf == {}:
        raise FileNotFoundError("There is no cloud configuration saved")
    return conf

def collection_connect():
    client = MongoClient(URI)
    db = client.get_database(env.MONGO_DATABASE)
    collection = db.get_collection(env.MONGO_COLLECTION)
    return collection
