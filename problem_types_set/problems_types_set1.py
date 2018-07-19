#1
print(int(2.9))
print(int(-2.5))
#2
year = input('Year of birth:')
print(2018-int(year))
#3
a = input('Value of a')
b = input('Value of b')
c = input('Value of c')
print((a>b>c) or (a<b<c))
4
import random
leapyear = random.randint(1000, 2018)
print(leapyear)
print('Was', leapyear, 'a leap year?', end='')
print(' ', int(leapyear)%4==0 and (int(leapyear)%400==0 or int(leapyear)%100!=0))
