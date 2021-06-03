from pymongo import MongoClient

from pymongo import MongoClient
import json
from mongoService import  MongoClientService


def main():
    mongo = MongoClientService(db_name="db", collection_name="comments",
                               host="localhost",
                               port=27017,
                               username="mongodbuser",
                               password="mongoPassword"
                               )
    all = mongo.readAll()

    for doc in all:
        print(doc)  # or do something with the document
if __name__ == "__main__":
    main()
