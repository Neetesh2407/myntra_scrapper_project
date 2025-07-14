from pymongo import MongoClient

class mongo_operation:
    def __init__(self, client_url, database_name):
        self.client = MongoClient(client_url)
        self.db = self.client[database_name]

    def bulk_insert(self, data, collection_name):
        collection = self.db[collection_name]
        if isinstance(data, list):
            collection.insert_many(data)
        else:
            collection.insert_many(data.to_dict(orient="records"))

    def find(self, collection_name):
        collection = self.db[collection_name]
        return list(collection.find())
