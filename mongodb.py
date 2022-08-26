import pymongo
client = pymongo.MongoClient("mongodb+srv://chetansingh:csksingh123@chetan.1j7pvw8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "chetan",
    "email" : "chetan@email.com"
}

db1 = client['mongodb']
coll = db1['test']
coll.insert_one(d)