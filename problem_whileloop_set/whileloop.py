import random
rng = random.randint(0,10)
print(rng)
guess = int(input('Guess a number'))
while rng != guess:
    if guess > rng:
        print('Too high.', end=' ')
    else:
        print('Too low.', end=' ')
    guess = int(input('Guess a number'))
else:
    print('Correct')
