from pymongo import MongoClient

from pymongo import MongoClient
import sys


class MongoClientService:
    def __init__(self, db_name, collection_name, host, port, username, password):
        try:
            client = MongoClient(host=host,
                                 port=int(port),
                                 username=username,
                                 password=password
                                 )
            self.db = client[db_name][collection_name]
        except:
            print("Server had problem while trying connecting  with mongodb.")
            print("Oops!", sys.exc_info()[0], "occurred.")

    def create(self, userName, description, commentsSet):
        self.db.insert_one({'author_name': userName, 'description': description, 'commentsSet': commentsSet})
        
    def readOne(self, id):
       return self.db.find_one({'id': id})
      
    def readAll(self):
       return self.db.find()
      
    def updateComment(self, id, comment):
        self.db.updateOne({'id': id}, {'$set': {'comment': comment}})
        
    def updateDesc(self, id, describe):
        self.db.updateOne({'id': id}, {'$set': {'describe': describe}})

    def updateAuthor(self, id,userName):
         self.db.updateOne({'id': id}, {'$set': {'authorName': userName}})