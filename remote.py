from urllib.parse import quote_plus

from pymongo import MongoClient


def get_mongo_collection(
    user: str, password: str, host: str, database_name: str, collection_name: str
):
    URI = "mongodb+srv://%s:%s@%s" % (
        quote_plus(user),
        quote_plus(password),
        host,
    )
    client = MongoClient(URI)
    db = client.get_database(database_name)
    collection = db.get_collection(collection_name)
    return collection
