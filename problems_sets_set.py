#Exercise 1
# residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
# print(residents['Sloth'])
#
# menu = {}
# menu['Sunday']= 16.78
# menu['Monday']= 20
# menu['Tuesday']= 18
#
# for k in menu:
#     print(k, ":", menu[k])
#
# # key - animal_name : value - locationzoo_
# animals = {'Unicorn' : 'Cotton Candy House',
#             'Sloth' : 'Rainforest Exhibit',
#             'Bengal Tiger' : 'Jungle House',
#             'Atlantic Puffin' : 'Arctic Exhibit',
#             'Rockhopper Penguin' : 'Arctic Exhibit'}
# del animals['Sloth']
# del animals['Bengal Tiger']
# animals['Rockhopper Penguin'] = 'Birds'
# print(animals)
#
# webster = {"Aardvark" : "A star of a popular children's cartoon show.",
#            "Baa" : "The sound a goat makes.",
#            "Carpet": "Goes on the floor.",
#            "Dab": "A small amount."
#            }
# for k in webster:
#     print(webster[k])
#
# my_dict = {"title" : "Stranger Things",
#            "is_show": True,
#            "seasons" : 2}
# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())
#
# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'],
#     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# }
#
# inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# inventory['backpack'].sort()
# inventory['backpack'].remove('dagger')
# inventory['gold'] += 50
# print(inventory)

#Exercise 2
# prices = {"banana": 4,
#           "apple": 2,
#           "orange": 1.5,
#           "pear": 3}
#
# stock = {"banana": 6,
#          "apple": 0,
#          "orange": 32,
#          "pear": 15}
# for k in prices:
#     print(k)
#     print('price:', prices[k])
#     print('stock:', stock[k])
# total = 0
# for k in prices:
#     print(prices[k] * stock[k])
#     total += prices[k] * stock[k]
# print(total)
#
# def compute_bill(food):
#     total = 0
#     for k in food:
#         if stock[k] > 0:
#             total += food[k]
#             stock[k] -= 1
#     return total
# print(compute_bill(prices))
# print(stock)

#Exercise 3
lloyd = {"name": "Lloyd",
         "homework": [90.0,97.0,75.0,92.0],
         "quizzes": [88.0,40.0,94.0],
         "tests": [75.0,90.0]}
alice = {"name": "Alice",
         "homework": [100.0, 92.0, 98.0, 100.0],
         "quizzes": [82.0, 83.0, 91.0],
         "tests": [89.0, 97.0]}
tyler = {"name": "Tyler",
         "homework": [0.0, 87.0, 75.0, 22.0],
         "quizzes": [0.0, 75.0, 78.0],
         "tests": [100.0, 100.0]}
students = [lloyd, alice, tyler]
for i in students:
    for k in i:
        print(i[k])

def average(numbers):
    total = float(sum(numbers))
    total = total / len(numbers)
    return total

