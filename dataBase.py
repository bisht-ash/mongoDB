import pymongo
import subprocess
def load():
  subprocess.call(["mongoimport","-d","mflix","-c","movies","--file","./Data/movies.json"])
  subprocess.call(["mongoimport","-d","mflix","-c","comments","--file","./Data/comments.json"])
  subprocess.call(["mongoimport","-d","mflix","-c","theaters","--file","./Data/theaters.json"])
  
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

try:
  mydb = myclient["mflix"]
except:
  load()
  mydb = myclient["mflix"]

commentsCollection=mydb["comments"]
moviesCollection=mydb["movies"]
theatersCollection=mydb["theaters"]