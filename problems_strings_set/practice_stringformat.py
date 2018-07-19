things = ['camera', 'couch', 'potato salad', 'energy drink', 'comb', 'suitcase']
prices = [50, 100, 5, 5, 1, 25]
for x in range(len(things)):
    print('{}: ${:.2f}'.format(things[x].rjust(15), prices[x]))
