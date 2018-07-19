# text = ('How are you today good sir? I hope you are well.')
# t = tuple(text.split())
# print(t)
# print(len(t))
#
# for x in ('Kathy', 'Benji', 'Ian', 'Alejandro'):
#     print(len(x))
#
import random
male = ('Jared', 'Brandon', 'Daniel', 'Carlos', 'Alex', 'Sam', 'Bryant', 'Ray', 'Sharaf', 'John')
female = ('Martha', 'Mary', 'Kim', 'Sally', 'Kelly', 'Jill', 'Julia', 'Stephanie', 'Rachel', 'Susan')
lastnames = ('Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
             'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin')
number = int(input('How many names?'))
gender = input('Gender?')
for x in range (0, number):
    if gender == 'male':
        print(male[random.randint(0,9)], end=' ')
        print(lastnames[random.randint(0,19)])
    elif gender == 'female':
        print(female[random.randint(0,9)], end=' ')
        print(lastnames[random.randint(0, 19)])
    elif gender == 'mix':
        # rng = random.randint(1,2)
        # if rng == 1:
        #     print(male[random.randint(0, 9)], end=' ')
        #     print(lastnames[random.randint(0, 19)])
        # if rng == 2:
        #     print(female[random.randint(0, 9)], end=' ')
        #     print(lastnames[random.randint(0, 19)])
        mix = male + female
        print(mix[random.randint(0, 19)], end=' ')
        print(lastnames[random.randint(0, 19)])