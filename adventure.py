import time, random, sys

# Initial text when starting adventure.
def introStoryText():
    print(" In a distant land from centuries past, there was a test for any")
    print("Men and Women coming of age. On their 20th Birthday, They were to")
    print("survive 14 days within the wilderness on the outskirts of the")
    print("village, not coming back until the 14 days are up.")
    time.sleep(10)
    print(" Those who were unsuccessful in the challenge were forced to go")
    print("and become servants for the neighboring Lords that supplied food.")
    print("You still remember when your older sister failed the challenge,")
    print("and is now working the docks over in Daneport. Hopefully you")
    print("won't share the same fate...\n")
    time.sleep(10)
    print(" You can hear the elders calling you now, the ceremony is starting.\n")
    time.sleep(5)
    print(" The Chief Elder begins to speak...\n")
    time.sleep(3)
    print('"Follow your senses and use your gut, there are unforgiving beasts')
    print('and dangerous cliffs, and the occasional snaggle root. If you are')
    print('to pass this test, you will receive honor within the village, and"')
    print('will be able to live as a free man. All free villagers must be a"')
    print('positive contribution to society."\n')
    time.sleep(12)
    print('"Go forth now, and become one with the land... For if you fail,')
    print('you will be a servant under the rule of the Kingdom. If you are')
    print('able to succeed, the rewards will be Freedom to learn and do as')
    print('you please, within the realm of reason in our lands."\n')
    time.sleep(12)
    print("The adventure begins.\n\n")

# Stores messages to display, in a list such as [[Day 1 Start, Day 1 End],
# [Day 2 Start, Day 2 End], and so on, to be used in the function dayPrompt()
MESSAGES = [['You trek onwards through the plains, nearing the forest edge.',
             'You walk into the woods as the daylight fades, and setup camp.'],
            ['You wake up to the morning chill. Camp was safe for the night.',
             'After scouting the area, you decide it\'s safe to camp again.'],
            ['You wake up to the morning chill again... Time to start a fire.',
             'The fire next to the tent ought to be warm enough tonight...'],
            ['You rest better thanks to the warm fire. Morning has arrived.',
             'After a long day of gathering firewood & food, you fall asleep.'],
            ['You wake up to a blown over tent, and decide to move camp...',
             'You move camp into a dense thicket of trees, to stop wind.'],
            ['You were too tired to start a fire last night, so you light one.',
             'After a long day of finding firewood, you fall fast asleep.'],
            ['You wake up to the sound of raindrops on your tent roof...',
             'After a rainy day of tending the fire, you fall asleep.'],
            ['You start to question reality, and your existence... Is it real?',
             'After a long day of philosophy and foraging, you fall asleep.'],
            ['You wake up cold and fluttered, the fire went out last night.',
             'After getting the fire started, you ran out of energy (zZzZz)'],
            ['You wake up... By now you\'ve lost track of the days...',
             'You fall asleep, pondering how long you have been away.'],
            ['You wake up to the low embers of your fire slowly losing heat.',
             'You manage to restock on firewood, and find a tool-worthy rock.'],
            ['You dreamt of the hearth back home last night. You awaken...',
             'The stars overhead look beautiful... You fall asleep.'],
            ['A distant roar from the mountains wakes you up. Nothing close by.',
             'You sit next to the fire, and drift off into a deep sleep.'],
            ['Some time during the night you moved to the tent. You wake up.',
             'You begin to understand the reasoning of this test... zZzZz'],
            ['You wake up, and question how long you have been out here.',
             'Shouldn\'t someone have come out here by now?'],]

FOODS = ['Wild Berries', 'Forest Mushroom', 'Fern Leaf', 'Slug Meat']

# Display the winning message (displayed when player wins)
def displayWinningMessage():
    print('You are spotted by a Village Scout.')
    time.sleep(3)
    print('"Hello, Villager. The chief has sent me out into the Wild to come')
    print('and find you, and see what has become of you. It appears you have')
    print('survived the challenge, and may now return with me to the Village.')
    time.sleep(6)
    print('You\'re family was beginning to get worried you might not have')
    print('made it, since you didn\'t come back and claim forefit.')
    time.sleep(5)
    print('Let us eat this portion of Bread and Wine, and we shall return."')
    time.sleep(3)
    print('\nYou and the Village Scout return to the village...')
    time.sleep(3)
    print('\nThe Chief and your Family welcome you home. The chief speaks.')
    time.sleep(3)
    print('\n"You have proved yourself to be a worthy contribution to our')
    print('village, for you have survived the wilderness. You have seen the')
    print('perils that lie on the other side of these walls, that many take')
    time.sleep(6)
    print('for granted until they succeed or fail in the challenge. You may')
    print('choose a desired plot of land in the Commons, and now have all')
    print('rights of a Free man within our kingdom."')
    time.sleep(10)
    print('\n\nY O U   W I N\n\n')

# Displays losing message, which occurs when player dies or starves and becomes
# too weak to continue his journey.
def displayLosingMessage():
    print('You become too weak to move... You start to fall asleep...')
    print('Your wounds are too viscious to be healed in the wild...')
    time.sleep(3)
    print('You have fallen asleep for the last time, and are slowly dying.')
    print('Hopefully a Scout will find you in time, before you die of the')
    print('natural elements, bleed to death, or starve out.')
    time.sleep(5)
    print('\n\nG A M E   O V E R\n\n')

# Creates a player dictionary, which stores stats
def makeNewPlayer():
    character = {'Health': 20, 'Hunger': 'Well Fed', 'Food':[], 'Day': 1}
    return character

# Display your character's attributes
def displayStats(player):
    print('\n+----------------------------------+')
    print("Health:", player['Health'])
    print("Hunger:", player['Hunger'])
    print("Food  :", end=' ')
    for food in player['Food']:
        print(food,end=', ')
    print() #Add newline. Was going to add to next line, but had to line up ':'
    print("Day   :", player['Day'])
    print('+----------------------------------+')

# Decrease the Well Fed values from most full, to least full, and then
# finally death if the player reaches that point.
def increaseHunger(player):
    if player['Hunger'] == 'Well Fed':
        player['Hunger'] = 'Full'
    elif player['Hunger'] == 'Full':
        player['Hunger'] = 'Semi-Fed'
    elif player['Hunger'] == 'Semi-Fed':
        player['Hunger'] = 'Hungry'
    elif player['Hunger'] == 'Hungry':
        player['Hunger'] = 'Starving'
    elif player['Hunger'] == 'Starving':
        player['Hunger'] = 'Brink of Death'
    else:
        player['Hunger'] = 'Death by Starvation'

# Increase the Well Fed values from least full to most full, will
# happen after eating.
def decreaseHunger(player):
    if player['Hunger'] == 'Brink of Death':
        player['Hunger'] = 'Starving'
    elif player['Hunger'] == 'Starving':
        player['Hunger'] = 'Hungry'
    elif player['Hunger'] == 'Hungry':
        player['Hunger'] = 'Semi-Fed'
    elif player['Hunger'] == 'Semi-Fed':
        player['Hunger'] = 'Full'
    elif player['Hunger'] == 'Full':
        player['Hunger'] = 'Well Fed'

# Decrease health of player by hitpoints dealt, as long as the
# player has 1 hitpoint or more remaining.
def decreaseHealth(player, hitpoints):
    if player['Health'] >= 1:
        player['Health'] -= hitpoints

# Heal player by given amount of hitpoints, as long as health isn't full.
# If health is full after healing, the second if statement will return
# the Health back to default of 20.
def increaseHealth(player, hitpoints):
    if player['Health'] < 20:
        player['Health'] += hitpoints
    if player['Health'] > 20:
        player['Health'] = 20

# Increment the Day by 1, to simulate time passage.
def newDay(player):
    player['Day'] += 1

# Gives the player a new greeting message each morning
def dayMessage(player):
    index = (player['Day'] - 1)
    print(MESSAGES[index][0])
    time.sleep(2)
    print()

# Gives player a message at night, before sleeping
def nightMessage(player):
    index = (player['Day'] - 1)
    print(MESSAGES[index][1])
    time.sleep(2)
    print()

# Forage for a random food (selected from FOODS list), dependent
# on the chance value (chance must be 1-14, values random from 1-40)
def forageFood(player):
    chance = random.randint(1, 40)
    food = random.choice(FOODS)
    if chance < 12:
        player['Food'].append(food)
        print('You manage to forage some %s. \n' % (food))
        time.sleep(2)

# Ask the player which food they would like to eat from inventory.
def getFoodChoice(player):
    while True:
        choice = input('\nWhat do you want to eat? ')
        if choice in player['Food']:
            return choice
        else:
            print('You have selected invalid item (items are case sensitive).')
            print('Valid Food Items:')
            for food in player['Food']:
                print(food)

# Removes the food from player's inventory
def removeFood(player, foodChoice):
    foodIndex = player['Food'].index(foodChoice)
    player['Food'].pop(foodIndex)

# Get the food choice to eat from player, eat the food (remove from inventory),
# increase hitpoints (food heals), and decrease the hunger.
def eatFood(player):
    food = getFoodChoice(player)
    if (food == 'Wild Berries'):
        removeFood(player, food)
        increaseHealth(player, 2)
        decreaseHunger(player)
        print('You eat the berries... They hold you over, for now.')
    elif (food == 'Fern Leaf'):
        removeFood(player, food)
        increaseHealth(player, 3)
        decreaseHunger(player)
        print('You munch on the fern leaf... Tastes like salad.')
    elif (food == 'Forest Mushroom'):
        removeFood(player, food)
        increaseHealth(player, 4)
        decreaseHunger(player)
        decreaseHunger(player)
        print('You slice the mushroom and gobble it up... Tasty.')
    elif (food == 'Slug Meat'):
        removeFood(player, food)
        increaseHealth(player, 6)
        decreaseHunger(player)
        decreaseHunger(player)
        decreaseHunger(player)
        print('You cook the large slug over the fire... Gourmet eating!')
    time.sleep(3)
    print()

# Prompt the player if they want to quit, after typing the 'quit' command.
def quitGame():
    while True:
        choice = input('Do you really want to quit [Y/N]? :').lower()
        if (choice.startswith('y')):
            print('Thanks for playing.')
            sys.exit()
        elif (choice.startswith('n')):
            print('Good luck... Push through!')
        else:
            print('Invalid input, only Yes/No/Y/N/y/n')

# Get input from the player, on whether they would like to rest, or eat some
# food to increase the chances of survival.
def playerInput(player):
    while True:
        command = input('$> ').lower()
        if (command.startswith('h')):
            print(" This is a game about survival. You can type what you want to")
            print("do around the camp for the day. Valid commands include:")
            print(" Eat  - You will sustain yourself off the land while out,")
            print("        foraging for plants/insects. Type this to ingest.")
            print(" Rest - Do nothing but the normal daily routine of foraging")
            print("        for food. This is useful to ration your food.")
            print(" Quit - Exit the game")
        elif (command == 'eat'):
            eatFood(player)
            break
        elif (command == 'rest'):
            variance = random.randint(0, 2)
            if player['Day'] == 1:
                print('You hike onwards to find an area to setup camp.')
            else:
                if variance == 0:
                    print('You stoke the fire for the day...')
                elif variance == 1:
                    print('You sit around camp, conserving energy.')
                else:
                    print('You lay in the tent, watching the fire.')
            print()
            break
        elif (command == 'quit'):
            quitGame()
        else:
            print("Invalid input. Type 'help' or 'h' for help.")

# Random events can happen by chance, which adds variety. Sprained
# ankles, snake bites, fighting with a wild boar, etc.
def randomEvent(player):
    event = random.randint(1, 10)
    if (event == 1):
        print("While scouting for areas to forage, you stumble into a root")
        print("pocket and bruise your ankle.")
        decreaseHealth(player, 3)
    elif (event == 3):
        print("You thought that the bush was clear, but it wasn't... You")
        print("get bitten by a non-venemous Python, before it escapes.")
        decreaseHealth(player, 5)
    elif (event == 7):
        print("A boar rams into your leg, luckily it didn't hit an artery.")
        print("You manage to make your way up a small cliff face, and throw")
        print("rocks at the boar... It runs away.")
        decreaseHealth(player, 6)
    elif (event == 10):
        print("You manage to find a piece of un-rotted Deer carcass, there")
        print("must be a wolf pack in the area. You bring it back to camp")
        print("to cook up...")
        increaseHealth(player, 7)
        decreaseHunger(player)
        decreaseHunger(player)
    time.sleep(6)
    print()

# Sequence of events that happens daily and in order. First the daily message
# will occur, followed by a random event to add some variety and replayability.
# Each day has a asimilar sequence of events, which is a message, followed by
# a random event, and a random chance to forage for food. Then the stats of
# the player are displayed, and the player is asked for an input command.
# This is the main logic sequence / flow of execution of the main game loop.
def daySequence(player):
    dayMessage(player)     # First, display the daily message
    randomEvent(player)    # Followed by a random event (monster/trap)
    forageFood(player)     # Forage for food in morning
    displayStats(player)   # Then display the player stats,
    checkStatus(player)    # Check status before displaying choices
    playerInput(player)    # Ask player to eat/rest/etc.
    forageFood(player)     # Forage for food in evening
    randomEvent(player)    # Second chance for a random event
    displayStats(player)   # Display stats before sleep, to show progress today
    checkStatus(player)    # Check status again before displaying choices
    playerInput(player)    # Gives player second chance to eat.
    increaseHunger(player) # Increase the player's hunger
    nightMessage(player)   # Display the night message
    newDay(player)         # Increment day to pass time

# Checks to see if player has survived the required 2 weeks to win
def checkTime(player):
    time = player['Day']
    if time > 14:
        return True
    else:
        return False

# Check on the player's health
def checkHealth(player):
    health = player['Health']
    hunger = player['Hunger']
    # If player has lost HP from random events, return True
    if health <= 0:
        return True
    # If player starves to death, return true
    if hunger == 'Death by Starvation':
        return True
    # Otherwise if the if statements don't compute, return False (player alive)
    return False

# Check to see if player has either died or won game.
def checkStatus(player):
    if checkHealth(player):
        displayLosingMessage()
        input('Press ENTER (game will exit)')
        sys.exit()
    if checkTime(player):
        displayWinningMessage()
        input('Press ENTER (game will exit)')
        sys.exit()

# Game Start
print('V I L L A G E R \'S   A D V E N T U R E')
print(' *      *    *  ^   *      *         *')
print('  /\  *   *    ^ *     *     *   * /\  ')
print(' /  \  /\  * ^     *     * /\  *  /  \  ')
print('/____\/__\  ^  @ *____ *  /__\   /____\ ')
print('__||___||__.w._@_/\___\____||______||__')
time.sleep(3)
print()

# Set up the game variables
introStoryText()
player = makeNewPlayer()

# Game Loop
while True:
    daySequence(player)
