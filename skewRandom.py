from random import randint
from mango import *

class skewRandom:

    def __init__(self, one, two, three):
        self.oneCount = 1
        self.twoCount = 2
        self.threeCount = 3
        
    def percentageCalc(self):
        totalGames = self.oneCount + self.twoCount + self.threeCount
        oneP = int(round(self.oneCount*100/totalGames), 0)
        print(oneP)
        


#def computeSkew():
#            values = (tallies.find_one({"_id" : 1}))
#            oneCount = values.get("one")
#            twoCount = values.get("two")
#            threeCount = values.get("three")
#            skew = skewRandom(oneCount, twoCount, threeCount)
#            skew.percentageCalc()

skew = skewRandom()
skew.percentageCalc()