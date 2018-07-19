# def max_of_three (x, y, z):
#     return max (x, y, z)
#
#
# def sum_of_numbers(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
#
#
# def product_of_numbers(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total
#
#
# def reverse_string(word):
#     reverse = word[::-1]
#     return reverse
#
#
# def factorial(number):
#     answer = 1
#     while number != 0:
#         answer *= number
#         number -= 1
#     return answer
#
#
# #same as one on top
# def factorial(num):
#     answer = 1
#     for n in range (1, num+1):
#         answer *= n
#     return answer
#
#
# def check_range(number):
#     a = int(input('First number'))
#     b = int(input('Seocnd number'))
#     if number in range(a, b):
#         print('Yes')
#     else:
#         print('No')
#
#
# def chr_count(phrase):
#     upperchr = 0
#     lowerchr = 0
#     phrase = phrase.replace(' ', '')
#     for x in phrase:
#         if x.isalpha():
#             if x == x.upper():
#                 upperchr += 1
#             else:
#                 lowerchr += 1
#     answer = str(upperchr) + ' uppercase letters and ' + str(lowerchr) + ' lowercase letters.'
#     return answer
#
#
# def unique_list(numbers):
#     answer = set(numbers)
#     return answer
#
#
# def prime(num):
#     answer = 'Not prime'
#     if num == 1:
#         answer = 'Not prime'
#     elif num == 2:
#         answer = 'Prime'
#     else:
#         for x in range(2, num):
#             if num%x != 0 and num != x:
#                 return 'Prime'
#             else:
#                 return 'Not prime'
#     return answer
#
#
# def even_numbers(numbers):
#     answers = ()
#     for x in numbers:
#         if x%2 == 0:
#             answers += (x,)
#     return answers
#
#
# def perfect_numbers(number):
#     test_number = 1
#     divisors = ()
#     while test_number != number:
#         if number%test_number == 0:
#             divisors += (test_number,)
#         test_number += 1
#     if sum(divisors) == number:
#         answer = str(number) + ' is a perfect number.'
#     else:
#         answer = str(number) + " isn't a perfect number."
#     return answer
#
#
# def palindrome(word):
#     reverse = word[::-1]
#     if reverse == word:
#         answer = word + ' is a palindrome.'
#     else:
#         answer = word + " isn't a palindrome."
#     return answer
#
#
# def pascals_triangle(n):
#     t = (1, 1)
#     final_t = (1,)
#     if n == 1:
#         answer = 1
#     elif n == 2:
#         print(1)
#         print(t)
#     elif n >= 3:
#         print('(1)')
#         print(t)
#         for x in range (3, n+1):
#             new_t = ()
#             thesum = t[x-3] + t[x-2]
#             new_t = int(thesum)
#             final_t = ()
#             final_t += (new_t,)
#             y = x
#             while len(final_t) != x-2:
#                 new_t = ()
#                 y -= 1
#                 thesum = t[y - 3] + t[y - 2]
#                 new_t = int(thesum)
#                 final_t += (new_t,)
#             final_t += (1,)
#             final_t = final_t[::-1]
#             final_t += (1,)
#             t = final_t
#
#             print(t)
#
#
# def panagram(phrase):
#     letters = ()
#     lowerphrase = phrase.lower()
#     for x in lowerphrase:
#         if x.isalpha():
#             letters += (x,)
#     unique_letters = set(letters)
#     if len(unique_letters) == 26:
#         answer = '"' + phrase + '"' + ' is a panagram.'
#     else:
#         answer = '"' + phrase + '"' + ' is not a panagram'
#     return answer
#
#
# def square(x, y):
#     answers = ()
#     for x in range(x, y+1):
#         if x**2 in range(x, y+1):
#             answers += (x**2,)
#     return answers


def get_weight(x, planet = 'Earth', weight = 'pounds'):
    if weight == 'kilograms':
        x *= 0.45
        if planet == 'Mercury':
            return x * 0.38
        elif planet == 'Venus':
            return x * 0.91
        elif planet == 'Mars':
            return x * 0.28
        elif planet == 'Jupiter':
            return x * 2.34
        elif planet == 'Saturn':
            return x * 1.06
        elif planet == 'Uranus':
            return x * 0.92
        elif planet == 'Neptune':
            return x * 1.19
        elif planet == 'Pluto':
            return x * 0.06
    return x
print(get_weight(100, planet = 'Saturn', weight = 'kilograms'))


# if __name__ == 'main':
#     print(factorial(6))
#     print("I'm in the module")