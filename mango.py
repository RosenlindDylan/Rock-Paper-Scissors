import pymongo
import pprint

from pymongo import MongoClient
me = MongoClient()

# this is the database!
mango = me['rocks']

# this is a collection in the database!
tallies = mango['tallies']

tally = {
    "1" : "0",
    "2" : "0",
    "3" : "0"
}

tallies.insert_one(tally)
pprint.pprint(tallies.find_one())

