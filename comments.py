from dataBase import moviesCollection,commentsCollection
from pprint import pprint


class comments:
    def addComment(self,dict):
        commentsCollection.insert_one(dict)
        
    def top10UserWithMaxComment(self):
        pipe=[
            {"$group":{"_id":"$name","count":{"$sum":1} }},
            {"$sort":{"count":-1}},
            {"$limit":10},
            {"$project" : {"_id":0,"User":"$_id","count":1}}
        ]
        pprint(list(commentsCollection.aggregate(pipeline=pipe)))
    
    def top10MoviesWithMaxComment(self):
        pipe=[
            {"$group":{"_id":"$movie_id","count":{"$sum":1} }},
            {"$sort":{"count":-1}},
            {"$limit":10}
        ]
        for doc in commentsCollection.aggregate(pipeline=pipe):
            print("Title: " + moviesCollection.find_one({ "_id":doc["_id"] })['title'] + ", Count: " + str(doc['count']))
            
    def monthWiseComment(self,year):
        pipe=[
            { "$project": {"year":{"$year":"$date"} , "month":{"$month":"$date"} }},
            {"$match" : { "year":year }},
            {"$group" : {"_id" : "$month", "count" : {"$sum":1}}},
            {"$project": {"month":"$_id","count":1,"_id":0 }},
            {"$sort" : {"month":1 }}
        ]
        pprint(list(commentsCollection.aggregate(pipe)))


def main():
    obj=comments()
    print("""
            Enter Choice:
            1. Top 10 users with most comments
            2. Top 10 movies with most comments
            3. For a given year, comments made every month
            """)
    ch=int(input())
    if ch == 1:
        obj.top10UserWithMaxComment()
    elif ch==2:
        obj.top10MoviesWithMaxComment()
    elif ch==3:
        obj.monthWiseComment()
    else:
        print("Wrong choice")
        
        

if __name__ == "__main__":
    main()


