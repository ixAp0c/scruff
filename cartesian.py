# Thinking of game to write in this script... Need to brainstorm it first!
def drawMap():
    HLINE = '+---------+---------+---------+---------+---------+'
    VLINE = '|         |         |         |         |         |'
    print('0', end='')
    for xNumbs in '10 20 30 40 50'.split():
        print((' ' * 7), xNumbs, end='')
    print()
    for x in range(5):
        print(HLINE)
        print(VLINE)
    print(HLINE)

drawMap()
