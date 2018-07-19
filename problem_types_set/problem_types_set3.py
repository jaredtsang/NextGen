#1
word = input('Word: ')
print(word[0:2], end='')
print(word[-2:])
#2
word1 = input('Word: ')
firstchar = word1[0]
word1a = word1.replace(firstchar, '$')
word1b = word1a[1:]
print(firstchar+word1b)
