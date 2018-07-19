#2
#Want to apply for a job?
answer = input('Would you like to apply for a job?')
if answer == 'No':
    print('Good bye!')
elif answer == 'Yes':
    answer = input('Do you have job experience?')

#Job experience
if answer == 'No':
    print('You may apply for an entry-level position!')
elif answer == 'Yes':
    answer = input('How many years?')

#Number of years
if int(answer) > 3:
    print('You may apply for an advanced position.')
else:
    print('You may apply for a mid-level position.')

#3
#Hungry/money?
hungry = input('Are you hungry?')
money = input('Do you have money?')

#Conditionals
if hungry == 'Yes' and money == 'Yes':
    print('Here is a take-out menu.')
elif hungry == 'Yes' and money == 'No':
    print('Time to heat up left-overs...')
elif hungry == 'No' and money == 'Yes':
    print('Buy yourself something nice.')
elif hungry == 'No' and money == 'No':
    print("Let's read a book!")

#4
import random
#dice
dice_one = random.randint(1,6)
dice_two = random.randint(1,6)
print(dice_one)
print(dice_two)

#Conditionals
if dice_one == dice_two:
    print('win')
elif dice_one + dice_two == 6:
    print('win')
elif dice_one + dice_two == 3:
    print('win')
else:
    print('lose')