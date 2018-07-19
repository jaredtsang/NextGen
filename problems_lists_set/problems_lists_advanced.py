# things = ['hat', 'cat', 'book']
# for i in range(len(things)):
#     things[i] += 's'
# print(things)
#
# nums = [1, 2, 3, 4, 5, 6]
# for i in range(len(nums)):
#     nums[i] = nums[i]**2
# print(nums)
#
# weights = [
#     ['dog', 30],
#     ['mug', 2],
#     ['book', 4]
# ]
# print('A', weights[1][0], 'weighs', weights[1][1], 'pounds.')
#
# weights.append(['truck', 5000])
# print(weights)
#
# for i in weights:
#     print('A', i[0], 'weighs', i[1], 'pounds.')
#
# import random
# #Print the board
# battleship = [
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
# ]
# for i in range(len(battleship)):
#     battleship.append(['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'])
# for i in battleship:
#     for x in i:
#         print(x, end='')
#     print()
#
# #Starting variables
# prize_spot = [random.randint(1, 10), random.randint(1, 10)]
# print(prize_spot)
# player_guess = 0
#
# #Player input
# row = int(input('Row number?'))
# if row > 10 or row < 1 or row == '':
#     row = int(input('Number is not in the range. Row number?'))
# column = int(input('Column number?'))
# if column > 10 or column < 1 or column == '':
#     column = int(input('Number is not in the range. Column number?'))
#
# while len(prize_spot) > 0 and player_guess != 4:
#     for i in prize_spot:
#         #Correct guess
#         if row == i[0] and column == i[1]:
#             player_guess += 1
#             battleship[row - 1][column - 1] = 'o'
#             prize_spot.remove(i)
#             print(prize_spot)
#             for x in battleship:
#                 for y in x:
#                     print(y, end='')
#                 print()
#             print('Good try. Guess again.')
#         #Incorrect guess
#         if row != i[0] and column != i[1]:
#             player_guess += 1
#             battleship[row - 1][column - 1] = 'x'
#             for x in battleship:
#                 for y in x:
#                     print(y, end='')
#                 print()
#             print('Try again.')
#         row = int(input('Row number?'))
#         if row > 10 or row < 1 or row == '':
#             row = int(input('Number is not in the range. Row number?'))
#         column = int(input('Column number?'))
#         if column > 10 or column < 1 or column == '':
#             column = int(input('Number is not in the range. Column number?'))
#         # guess = [row, column]
#         # print(guess)
#     if player_guess == 4:
#         print('No more turns.')
# # while row != prize_spot[0] or column != prize_spot[1] and player_guess != 4:
# #     battleship[row - 1][column - 1] = 'x'
# #     for i in battleship:
# #         for x in i:
# #             print(x, end='')
# #         print()
# #     print('Try again.')
# #
# #     # Player input
# #     row = int(input('Row number?'))
# #     if row > 10 or row < 1 or row == '':
# #         row = int(input('Number is not in the range. Row number?'))
# #     column = int(input('Column number?'))
# #     if column > 10 or column < 1 or column == '':
# #         column = int(input('Number is not in the range. Column number?'))
# #
# #     #Number of guesses
# #     player_guess += 1
# # if player_guess == 4:
# #     print('No more turns.')
#
# #Correct
# if len(prize_spot) == 0:
#     print('You win!')

# prize_spot = [(1,2), (3,3)]
#
# user_guess_list = '1 2'.split()
# user_tuple = tuple(map(int,input('Guess').split()))
#
# r_g = int(user_guess_list[0])
# c_g = int(user_guess_list[1])
#
# # print(user_tuple)
# if (r_g, c_g) in prize_spot:
#     print('You got one')
#     prize_spot.remove((r_g, c_g))
#     print(prize_spot)
#
#
# x, y = map(int, input('Enter x y ').split())

import random
prizes = [[random.randint(0,9), random.randint(0,9)], [random.randint(0,9), random.randint(0,9)]]
print(prizes)

lightbright = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
board = []

for x in range(10):
    board.append(lightbright.copy())

for row in board:
    for dot in row:
        print(dot, end= ' ')
    print()

turns = 0
while turns < 10:
    user_guess = map(int, input('Enter a row and column (Example: 1 2):').strip().split())

    turns += 1
    print(y, x)
    if x == secret_x and y == secret_y:
        print('You found it')
        board[y][x] = 'X'
        turns = 0
    else:
        board[y][x] = 'o'

    for row in board:
        for dot in row:
            print(dot, end= ' ')
        print()