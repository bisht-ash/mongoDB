from dataBase import theatersCollection
from pprint import pprint


class theaters:
    def addMovies(self,dict):
        theatersCollection.insert_one(dict)
        
    def top10CitiesMostTheaters(self):
        pipe=[
            {"$group":{"_id":"$location.address.city","cnt":{"$sum":1}}},
            {"$sort":{"cnt":-1}},
            {"$limit":10}
        ]
        pprint(list(theatersCollection.aggregate(pipe)))
    def top10theatersNear(self,cod):
        pprint(list(theatersCollection.find(
        {
        "geo": {
            "$near": {
            "$geometry": {
                "type": "Point" ,
                "coordinates": cod
            },
            }
        }
        }).limit(10)))
        
def main():
    obj=theaters()
    print("""
            Enter Choice:
            1. Top 10 cities with most theaters
            2. Top 10 theaters nearby given co-ordinates
            """)
    ch=int(input())
    if ch == 1:
        obj.top10CitiesMostTheaters()
    elif ch==2:
        l=[]
        l.append(float(input("Enter Latitute: ")))
        l.append(float(input("Enter Longitude: ")))
        obj.top10theatersNear(l)
    else:
        print("Wrong choice")
        
        

if __name__ == "__main__":
    main()