from random import randint
from mango import *
import pprint

class skewRandom:

    def __init__(self, one, two, three):
        self.oneCount = one
        self.twoCount = two
        self.threeCount = three
        
    def percentageCalc(self):
        totalGames = self.oneCount + self.twoCount + self.threeCount
        oneP = round(self.oneCount*100/totalGames)
        twoP = round(self.twoCount*100/totalGames)
        threeP = round(self.threeCount*100/totalGames)
        return [oneP, twoP, threeP]