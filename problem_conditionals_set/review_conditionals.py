# word = input('Word?')
# if word[-1] == 'x' or word == 's':
#     print(word, 'es', sep='')
# elif word[-2:] == 'th' or word[-2:] == 'sh' or word[-2:] == 'ch':
#     print(word, 'es', sep='')
# else:
#     print(word, 's', sep='')

userbits = input('Number of bits?')
bits = int(userbits)
answer = 0
for x in range(0, bits):
    answer += 2**x
print(answer)