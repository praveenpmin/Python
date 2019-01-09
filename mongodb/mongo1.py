import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pythondb"]

mycol = mydb["customers"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "local" in dblist:
  print("The database exists.")