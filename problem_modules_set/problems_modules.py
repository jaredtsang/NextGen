# 1
import random

rng = random.randint(1, 10)
print(rng)
guess = input('Guess a number from 1 to 10: ')
print('Are you a winner?', end=' ')
if rng == int(guess):
    print('Yes')
else:
    print('No')
print('The secret number was ', rng, sep='')

# 2
import statistics

ages = (18,20,21,17,15,16,20,18,21,17,22,14,20)
print(statistics.median(ages))
print(statistics.mode(ages))
