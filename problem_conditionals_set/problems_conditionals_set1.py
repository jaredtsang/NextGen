#Set winning number
import random
wnum = random.randint(0,10)
print(wnum)
#Set message
wmsg = ('You win!')

#Get guess
guess = input('Guess a number')

#Conditionals
if int(guess) == wnum:
    print(wmsg)
elif int(guess) > wnum:
    print('That number is too high.')
else:
    print('That number is too low')
