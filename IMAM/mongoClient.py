from pymongo import MongoClient

from pymongo import MongoClient
import sys

class MongoClient:
    def __init__(self,db_name, host, port, username, password):
        try:
            client = MongoClient(host=host,
                                 port=int(port),
                                 username=username,
                                 password=password
                                )
            db_handle = client[db_name]
        except:
            print("Server had problem while trying connecting  with mongodb.")
            print("Oops!", sys.exc_info()[0], "occurred.")
    def returnDbHandle(self):
        return self.db_handle


class MongoTable:
    def __init__(self,db_handle, collection_name):
        db = db_handle[collection_name]

    def createBasicUserRecord(self, userName, userConfig, comments):
        self.db.inserOne({'userName': userName, 'userConfig': userConfig, 'comments': comments})

    def read(self, userName):
        self.db.find({'userName': userName}).limit(1)

    def updateConfig(self, userName, userConfig):
        self.db.updateOne({'userName': userName}, {'$set': {"userConfig": userConfig}})

    def updateComment(self, userName, comment):
        self.db.updateOne({'userName': userName}, {'$set': {"comment": comment}})

