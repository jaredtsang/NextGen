testgrade = input('What number grade did you get on the test?')
grade = int(testgrade)
if grade >= 93:
    print('A')
elif grade >= 90:
    print('A-')
elif grade >= 87:
    print('B+')
elif grade >= 85:
    print('B')
elif grade >= 83:
    print('B-')
elif grade >= 78:
    print('C+')
elif grade >= 76:
    print('C')
elif grade >= 72:
    print('C-')
elif grade >= 69:
    print('D+')
elif grade >= 66:
    print('D')
elif grade >= 63:
    print('D-')
else:
    print('F')

firstnum = input('First number?')
operation = input('Operation?')
secondnum = input('Second number?')
if operation == '+':
    print(int(firstnum)+int(secondnum))
elif operation == '-':
    print(int(firstnum)-int(secondnum))
elif operation == '*':
    print(int(firstnum)*int(secondnum))
elif operation == '/':
    print(int(firstnum)/int(secondnum))
elif operation == '^':
    print(int(firstnum)**int(secondnum))
elif operation == 'weird':
    print(int(firstnum) / 10000)
