from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
        

class MongoDBHelper:
    def __init__(self, collection="users"):
        
        uri = "mongodb+srv://nainagupta9914:1234@cluster0.xmcswke.mongodb.net/?appName=Cluster0"

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        
        self.db = self.client['gw2810']
        self.collection = self.db[collection]

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document inserted in Collection:", self.collection.name)
        print("result is:", result)
        return result

    def fetch(self, query=""):
        
        documents = self.collection.find(query)
        return list(documents)

    def delete(self,query=""):
        documents=self.collection._delete_one(query)
        result=self.collection,delete_one(query)
        print("result is:",result)
        return result
        
    def update(self,document,query):
        document_to_update={'$set': document}
        result=self.collection.update_one(query,document_to_update)
        print("RESult is:", result)
        return result