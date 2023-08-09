from random import randint
from mango import *
from skewrandom import skewRandom

class playGame():
    '''
        just a fun project to mess around with some ideas that i have!
        constructor keeps games going while the user answers anything starting with 'y'    
        game itself is a simply rock paper scissors vs a computer
        the 'computer' tracks the user's choices to skew its random selection to counteract
            whatever the user picks most frequently more frequently than its other choices
        mongodb local database methods and setup are all in mango.py
        random skew methods are in skewrandom.py
        autotestsrps.py is a work in progress that will have 'computer' vs 'computer'
            with each tracking eachother's answer choices and skewing theirs accordingly
    '''

    def __init__(self):
        print('welcome! do you want to play rock paper scissors? (y/n)')
        ans = input()
        while ans not in ('y','n'):
            print('please retry, do you want to play rock paper scissors? (y/n)')
        while ans == 'y':
            self.newGame()
            print('do you want to play again? (y/n)')
            ans = input()
            while ans not in ('y','n'):
                print('please retry, do you want to play again? (y/n)')
                ans = input()

    # performs full game functionality
    def newGame(self):
        # get the user input here
        print('rock (1), paper (2), scissors (3) ...')
        userChoice = int(input())
        while userChoice != 1 and userChoice != 2 and userChoice != 3:
            print('rock (1), paper (2), scissors (3) ...')
            userChoice = int(input())
        print('... shoot!')

        # function to update the db with the user selection each round
        def updateDB():
            # dict to convert number to word
            nums = {
                1 : 'one',
                2 : 'two',
                3 : 'three'
            }
            choice = nums.get(userChoice)
            newT = mango["tallies"].update_one(
                {"_id" : 1},
                {"$inc":
                   {choice: 1}
                }
            )
        updateDB()

        # this calculates the skew matrix based on the number of times each user option has
        # been chosen, the skew matrix is percentage based and used to make the computer more
        # more likely to beat the user, while still allowing for a random element
        def computeSkew():
            values = (tallies.find_one({"_id" : 1}))
            oneCount = values.get("one")
            twoCount = values.get("two")
            threeCount = values.get("three")
            skew = skewRandom(oneCount, twoCount, threeCount)
            return skew.percentageCalc()

        skews = computeSkew()
        # apply the skew to a random to get computer selection based on the probability matrix
        selRange = randint(0,100)
        if selRange < skews[0]:
            computer = 1
        elif selRange < skews[1]:
            computer = 2
        else:
            computer = 3

        # word / number conversion
        def num_to_word(int):
            if int == 1:
                return 'rock'
            elif int == 2:
                return 'paper'
            else:
                return 'scissors'

        print('the computer chose ' + num_to_word(computer))

        # calculate if player wins or not
        if (userChoice == computer):
            print('you tied!')
        elif (userChoice - computer) == (1 or -2):
            print('you won!')
        else:
            print('you lost!')