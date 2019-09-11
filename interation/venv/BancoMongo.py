from pymongo import MongoClient

client = MongoClient()
db = client.test

#colletionAnwsers = db["vocabulo1"]
db.colletionAnwsers.find( {} )
print(db.list_collection_names())


def get_response_model(self):
    from chatterbot.conversation import Response
    # Create a storage-aware response
    response = Response
    response.storage = self

    return response

def count(self):
    return self.statements.count()
