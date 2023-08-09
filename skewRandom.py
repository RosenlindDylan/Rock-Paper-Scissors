
class skewRandom:

    # passes in the counts for user selections
    def __init__(self, one, two, three):
        self.oneCount = one
        self.twoCount = two
        self.threeCount = three
        
    # calculates the percentages each choice is selected
    # returns as a list
    def percentageCalc(self):
        totalGames = self.oneCount + self.twoCount + self.threeCount
        oneP = round(self.oneCount*100/totalGames)
        twoP = round(self.twoCount*100/totalGames)
        threeP = round(self.threeCount*100/totalGames)
        return [oneP, twoP, threeP]