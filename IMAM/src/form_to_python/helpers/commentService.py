import json
from bson.objectid import ObjectId
from mongo.mongoService import MongoClientService

mongo = MongoClientService("db", "comments", "localhost", 27017, "mongodbuser", "mongoPassword")
comments = []

def configure_record(request):
    tags = request.POST.get('tags').split()

    setting = {
        'author_name': request.POST.get('author_name'),
        'description': request.POST.get('description'),
        'commentsSet': [{
            'mandatory_words': tags,
            'comments': comments
        }]
    }
    setting_json = json.dumps(setting)  # json format
    setting_dict = json.loads(setting_json)
    mongo.db.insert_one(setting_dict)
    comments.clear()
    comments_list = read_all()
    return comments_list


def add(request):
    single_comment = request.POST.get('comment')
    comments.append(single_comment)
    return comments


def clear():
    comments.clear()


def read_all():
    comments_list = []
    all = mongo.readAll() # read all comments form db
    for comment in all:
        comments_list.append(comment)
    return comments_list


def delete(_id):
    mongo.db.delete_one({'_id': ObjectId(_id)})

def read_one(_id):
    record = mongo.db.find_one({'_id': ObjectId(_id)})
    print(record)
    return record
