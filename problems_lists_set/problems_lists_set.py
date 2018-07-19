# shopping_list = []
# item = input('Input an item.')
# while item != '':
#     shopping_list.append(item)
#     item = input('')
# else:
#     for r in shopping_list:
#         print(r, end='\n')
#
# main_course = ['steak', 'salmon', 'rice']
# main_course.insert(0, 'stew')
#
# # addedcourses = input('Type in at least 3 more main courses')
# # addedcourses = addedcourses.split()
# # main_course.extend(addedcourses)
# main_course.extend(input('Type in at least 3 more main courses').split())
# print('Ok, the main courses are now:', main_course)
#
# sides = ['carrots', 'fries', 'salad']
# style = ['seared', 'boiled', 'baked']
# import random
# print('Tonight I will serve', random.choice(style), random.choice(main_course), 'with', random.choice(sides))
#
# calculator = []
# calculator.extend(input('').split())
# if calculator[1] == '+':
#     print(int(calculator[0]) + int(calculator[2]))
# elif calculator[1] == '-':
#     print(int(calculator[0]) - int(calculator[2]))
# elif calculator[1] == '*':
#     print(int(calculator[0]) * int(calculator[2]))
# elif calculator[1] == '/':
#     print(int(calculator[0]) / int(calculator[2]))
#
# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers
# print(sum_list([1,2,-8]))
#
#
# def product_list(items):
#     product_numbers = 1
#     for x in items:
#         product_numbers *= x
#     return product_numbers
# print(product_list([1,2,-8]))
#
#
# def max_list(items):
#     max = items[0]
#     for x in items:
#         if x > max:
#             max = x
#     return max
# print(max_list([1, 2, -8, 0]))
#
#
# def min_list(items):
#     min = items[0]
#     for x in items:
#         if x < min:
#             min = x
#     return min
# print(min_list([1, 2, -8, 0]))
#
#
# def string_checker(strings):
#     validstrings = 0
#     for x in strings:
#         if len(x) >= 2 and x[0] == x[-1]:
#             validstrings += 1
#     return validstrings
# print(string_checker(['abc', 'xyz', 'aba', '1221']))
#
#
# def last(n): return n[-1]
#
# def sort_list_last(tuples):
#   return sorted(tuples, key=last)
#
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
#
#
# def remove_duplicates(sample_list):
#     return list(set(sample_list))
# print(remove_duplicates(['a', 'b', 'c', 'a']))
#
#
# def empty_check(sample_list):
#     checker = 0
#     answer = 'Empty'
#     for x in sample_list:
#         checker += 1
#     if checker != 0:
#         answer = 'Not empty'
#     return answer
# print(empty_check([]))
#
#
# def copy_list(sample_list):
#     copiedlist = sample_list
#     return sample_list, copiedlist
# print(copy_list(['a', 'b', 'c', 'a']))
#
#
# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))
#
#
# def common_list(list1, list2):
#     answer = False
#     for x in list1:
#         if x in list2:
#             answer = True
#     return answer
# print(common_list(['1'], ['2', '3']))


def remove_list(items):
    del items[0]
    del items[2]
    del items[2]
    return items
print(remove_list(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))