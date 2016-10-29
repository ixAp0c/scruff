import random

print('-- Numbers Guessing Game --')
print('-- (numbers from 1-100) ---')

number = random.randrange(100) # Generate random int 1-100
low = high = 0 # Keeps score of low / high guesses

for i in range(7):
    guess = int(input('Guess the number: '))
    if((guess > 100) or (guess <= 0)):
        print('Invalid input, numbers range from 1-100. Exiting.')
        break
    elif(guess > number):
        print('Too high.\n')
        high = high + 1
    elif(guess < number):
        print('Too low.\n')
        low = low + 1
    # Keeps track of high / low guesses
    print('Low guesses:  ', low)
    print('High guesses: ', high)
    print('Guesses left: ', 7 - (high + low), '\n')

if(guess == number):
    print('You win! You guessed', guess, 'which is equal to', number)
elif(guess > 100 or guess <= 0):
    pass
else:
    print('You lose... Better luck next time, chump.')
