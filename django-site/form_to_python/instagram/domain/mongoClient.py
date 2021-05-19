from pymongo import MongoClient


class Mongo:
    db = MongoClient().aggregation_example

    def createBasicUserRecord(self, userName, userConfig, comments):
        self.db.things.inserOne({'userName': userName, 'userConfig': userConfig, 'comments': comments})

    def read(self, userName):
        self.db.find({'userName': userName}).limit(1)

    def updateConfig(self, userName, userConfig):
        self.db.things.updateOne({'userName': userName}, {'$set': {"userConfig": userConfig}})

    def updateComment(self, userName, comment):
        self.db.things.updateOne({'userName': userName}, {'$set': {"comment": comment}})

