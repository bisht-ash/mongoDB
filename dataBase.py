import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mflix"]

commentsCollection=mydb["comments"]
moviesCollection=mydb["movies"]
theatersCollection=mydb["theaters"]