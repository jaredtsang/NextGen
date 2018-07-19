#1
for firstrange in range(0, 99):
    if firstrange%3 == 0:
        print(firstrange)

#2
sevens = -1
for secondrange in range(0,200):
    if secondrange%7 == 0:
        print(secondrange)
        sevens+=1
print(sevens)

#3
for thirdrange in range (7, 0, -1):
    print('2 to the', thirdrange, 'is', 2**thirdrange)

#4
firstname = input('What is your name?')
for firstname in (firstname):
    print(firstname)

#5
secondname = input('What is your name?')
for vowel in secondname:
    if vowel in 'aeiou':
        print(vowel)

#6
thirdname = input('What is your name?')
for thirdname in thirdname:
    binarythirdname = (bin(ord(thirdname)))
    print(binarythirdname[2:])
