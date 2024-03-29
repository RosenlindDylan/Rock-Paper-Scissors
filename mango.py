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

# pretty prints whole db so you can check values
def printDB():
    pprint.pprint(tallies.find_one())

# reset db
def clearDB():
    tallies.delete_many({})
    insertBlank()
