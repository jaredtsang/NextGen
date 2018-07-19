import re
import sys
try:
    f = open('z/Users/Jared Tsang/Desktop/harrypotter.txt', 'r')
except:
    print('File error')
    print(sys.exc_info()[0])


# text = f.read()
# f.close()
# harry_quotes = re.findall('".*".*Harry*', text)
# for quote in harry_quotes:
#     print(quote)
# print(len(harry_quotes))
#
# ron_quotes = re.findall('".*".*Ron*', text)
# for quote in ron_quotes:
#     print(quote)
# print(len(ron_quotes))
#
# hermione_quotes = re.findall('".*".*Hermione*', text)
# for quote in hermione_quotes:
#     print(quote)
# print(len(hermione_quotes))