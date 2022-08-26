import pymongo

client = pymongo.MongoClient("mongodb://chetansingh:csksingh12@ac-fykxlmj-shard-00-00.v1myowb.mongodb.net:27017,ac-fykxlmj-shard-00-01.v1myowb.mongodb.net:27017,ac-fykxlmj-shard-00-02.v1myowb.mongodb.net:27017/?ssl=true&replicaSet=atlas-ok2jzh-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"chetan"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
