import random
import time
import os

# Set list to empty (pass by reference), and create a die from the
# empty list, turning it into a list with [1, 2, 3, 4, 5, 6]
def createDie(d):
    for i in range(1, 7):
        d.append(i)

# Creates pair of dice, calling createDie() twice
def createDicePair(d1, d2):
    createDie(d1)
    createDie(d2)

# Roll single die (shuffles list referenced as d)
def rollDie(d):
    random.shuffle(d)

# Roll pair of dice, shuffling both lists
def rollDicePair(d1, d2):
    rollDie(d1)
    rollDie(d2)

# Roll dice and get results (will return first index from shuffled list) 
def rollAndGetResults(d1, d2):
    rollDicePair(d1, d2)
    r1, r2 = d1[0], d2[0]
    return r1, r2

# Checks for winner (two of a kind, both dice rolled same digit)
def checkWinner(r1, r2):
    if not (r1==r2):
        return False
    else:
        return True

# Prompts user to roll, to give game a bit of flow; takes roll number
# to give correct messages, along with a bit of variance
def promptRoll(rollNumber):
    roll = ''
    while (roll != 'r' and roll != 'R'):
        rollsLeft = 5 - rollNumber
        if (rollNumber == 0):
            print('"Roll one with the magical dice..." (press R)')
            roll = input()
        elif (rollNumber < 4):
            print('"Try again, you have %s more tries (press R)."' % rollsLeft)
            roll = input()
        else:
            print('"Last try, then I have to fly!" (press R)')
            roll = input()
    return roll

def displayIntro():
    print()
    print('You are resting in a tavern, tired from your journey.')
    time.sleep(2)
    print('A mysterious old man approaches, dressed in a smelly garb...\n')
    time.sleep(3)
    print('"Hello! I am a traveler... I hold the secrets of many lands.')
    time.sleep(3)
    print('Roll a two of a kind, with these magical dice. Then you')
    print('may learn a fortune.')
    time.sleep(3)
    print('You have 5 tries.')

def displaySecrets():
    os.system('fortune')

def displayRoll(r1, r2):
    print('"You roll...', end=' ')
    time.sleep(3)
    print('a %s and %s."' % (r1, r2))

# Ask user to play again
def playAgain():
    print('\nWould you like to play again?')
    return input().lower().startswith('y')

displayIntro()
while True:
    d1, d2 = [], []
    createDicePair(d1, d2)

    rollCount = 0
    while (rollCount < 5):
        promptRoll(rollCount)
        r1, r2 = rollAndGetResults(d1, d2)
        if checkWinner(r1, r2):
            displayRoll(r1, r2)
            displaySecrets()
            break
        else:
            displayRoll(r1, r2)
        rollCount += 1

    time.sleep(2)
    if not playAgain():
        break
