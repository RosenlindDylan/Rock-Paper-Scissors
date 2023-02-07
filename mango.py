import pymongo
import pprint
from pymongo import MongoClient

me = MongoClient()

# this is the database!
mango = me['rocks']

# this is a collection in the database!
tallies = mango['tallies']

# inserts blank tallies count
def insertBlank():
    count = {
        "_id": 1,
        "one" : 0,
        "two" : 0,
        "three" : 0
    }
    tallies.insert_one(count)

# pretty prints whole db
def printDB():
    pprint.pprint(tallies.find_one())

# just clears db and inserts blank count back
def clearDB():
    tallies.delete_many({})
    insertBlank()
