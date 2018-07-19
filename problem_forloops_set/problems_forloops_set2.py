# #1
# for row in range(9):
#     for column in range(9):
#         print('*', end='')
#     print()
#
#3
start = 1
arrow = input("Put in a number")
arrow1 = int(arrow)-1
print('*')
for length in range (1, (int(arrow)-1)):
    while start < int(arrow):
        start+=1
        print('*'*int(start))
print('*'*(int(arrow)-1))
for length in range(arrow1, 1, -1):
    while arrow1 >= 1:
        arrow1-=1
        print('*'*arrow1)


for i in range(1, int(arrow) + 1):
    for x in range(1, i+1):
        print('*', end=" ")
    print()
for i in range(int(arrow) - 1, 0, -1):
    for x in range(i, 0, -1):
        print('*', end=" ")
    print()

for i in range(0, int(arrow)):
    print(i*'*')
for i in range(int(arrow), 0, -1):
    print(i*'*')