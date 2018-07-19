#1. Backwards guessing game
import random
print('Think of a number between 1 and 10. I’m going to guess. Ready?')
x = random.randint(1,10)
print('Is it', x, '?', end= ' ')
answer = input()
guessbank = (0,)
# guessnum = 0
while answer != 'yes':
    if answer == 'no' or answer == 'NO' or answer == 'No' or answer == 'nO':
        # guessnum+=1
        x = random.randint(1, 10)
        while x in guessbank:
            x = random.randint(1, 10)
        guessbank = guessbank + (int(x),)
        print('Is it', x, '?', end= ' ')
        answer = input()
    # if guessnum >= 2:
    #     print('I lost!')
    #     break
    if answer == 'yes':
        print('I won!')
