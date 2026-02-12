from os import getenv
from functools import lru_cache

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

if getenv("ENVIRONMENT") != "production":
    load_dotenv()

uri = getenv("MONGODB_CONNECTION_STRING")


@lru_cache(maxsize=1)
def get_database_connection():
    # Create a new client with connection pooling
    client = MongoClient(
        uri,
        maxPoolSize=50,  # Adjust based on your application needs
        retryWrites=True,
        connectTimeoutMS=5000,
        serverSelectionTimeoutMS=5000,
    )
    return client.portal


# Get database instance
db = get_database_connection()
