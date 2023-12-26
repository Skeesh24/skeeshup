from urllib.parse import quote_plus

from pymongo import MongoClient


def get_mongo_collection(
    user: str, password: str, host: str, database_name: str, collection_name: str
):
    """
    Open a new connection through the MongoClient and returned requesting collection
    :param user: mongodb username
    :param password: mongodb password
    :param host: mongodb host part of the connection string
    :param database_name: requested mongodb database name
    :param collection_name: requested mongodb collection name
    """
    URI = "mongodb+srv://%s:%s@%s" % (
        quote_plus(user),
        quote_plus(password),
        host,
    )
    client = MongoClient(URI)
    db = client.get_database(database_name)
    collection = db.get_collection(collection_name)
    return collection
