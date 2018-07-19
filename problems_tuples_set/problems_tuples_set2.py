# import random
# answerwords = ('dog', 'bird', 'truck')
# word = answerwords[random.randint(0,2)]
# numberguesses = 0
# print(word)
# for letter in word:
#     print('_', end='')
# print(' ', len(word), 'letters')
# all_letters_tuple = tuple()
# all_tuples = tuple()
# guess = (input('Guess a letter').lower())
# correctguesses = tuple()
# # all_tuples += (guess,)
# while len(word) > len(correct_guesses):
#     if guess in all_tuples:
#         input('Guess again.')
#     else:
#         # all_tuples += (guess,)
#     for letter in word:
#         if letter in correctguesses:
#             print(letter, end='')
#         elif guess in letter:
#             correctguesses += (guess,)
#             print(guess, end='')
#         else:
#             print('_', end='')
#     # print()
#     # print(all_tuples)
#     guess = (input('Guess again').lower())
# print(word, 'You win!', sep='\n')

# import urllib.request
# webpage = urllib.request.urlopen('http://www.gutenberg.org/files/43/43-0.txt')
# all_text = webpage.read().decode('UTF-8')
# print(all_text)
#
# import random
#
# wordlist = ('dog', 'bird', 'truck')
# word = random.choice(wordlist)
# correct_guesses = tuple()
# num_turns = 0
# all_letters = tuple()
#
# print(word)
#
# for letter in word:
#     print('_', end=' ')
#
# print()
# player_letter = input('\nGuess a letter')
# player_letter = player_letter.lower() #make the case not matter
# all_letters += (player_letter,)  #save the guess
# # Check for correct answer
# if player_letter in word:
#     print('Good guess!')
#     correct_guesses += (player_letter,)  # saves correct answer
#
# #Prints the board
# for w in word:
#     if w in correct_guesses:
#         print(w, end=' ')
#     else:
#         print('_', end=' ')
#
# #Allow 6 guesses
# while len(word) > len(correct_guesses) and num_turns < 5:
#     num_turns += 1 #count the turn
#
#     print()
#     print(num_turns)
#
#     print('You have already guessed', all_letters)
#
#     player_letter = input('\nGuess a letter')
#     #Don't let them repeat
#     while player_letter in all_letters:
#         print('You guessed that already!')
#         player_letter = input('\nGuess a letter:')
#
#     player_letter = player_letter.lower()
#     all_letters += (player_letter,)
#
#     #Check for correct answer
#     if player_letter in word:
#         print('Good guess!')
#         correct_guesses += (player_letter,) #saves correct answer
#
#     #Prints the board
#     for w in word:
#         if w in correct_guesses:
#             print(w, end=' ')
#         else:
#             print('_', end=' ')
#
# #tell them if they won or lost
# if len(word) > len(correct_guesses):
#     print('\nSorry you lost. The word was', word)
# else:
#     print('\nYou got it!')
import random
import matplotlib.pyplot as plt
with open('/Users/Jared Tsang/Desktop/harrypotter.txt', 'r') as file:
    text = file.read()

text = text.lower()

text = text.replace(',', '')
text = text.replace(':', '')
text = text.replace('.', '')
text = text.replace('?', '')
text = text.replace('(', '')
text = text.replace(')', '')
text = text.replace('"', '')
text = text.replace('!', '')
text = text.replace(';', '')
text = text.replace('-', '')

tlist = text.split()

print(len(tlist))

print('Harry appears:', tlist.count('harry'))
print('Hermoine appears:', tlist.count('hermione'))
print('Ron appears:', tlist.count('ron'))
print('Hagrid appears:', tlist.count('hagrid'))

print('Unique word count:', len(set(tlist)))

ulist = list(set(tlist))


plt.bar(['total words', 'unique words'], [len(tlist), len(ulist)])
plt.show()

plt.scatter(['total words', 'unique words'], [len(tlist), len(ulist)])
plt.show()

plt.plot(['total words', 'unique words'], [len(tlist), len(ulist)])
plt.show()

#Hangman game
# word = random.choice(unique_list)
# correct_guesses = tuple()
# num_turns = 0
# all_letters = tuple()
#
# print(word)
#
# for letter in word:
#     print('_', end=' ')
#
# print()
# player_letter = input('\nGuess a letter')
# player_letter = player_letter.lower() #make the case not matter
# all_letters += (player_letter,)  #save the guess
# # Check for correct answer
# if player_letter in word:
#     print('Good guess!')
#     correct_guesses += (player_letter,)  # saves correct answer
#
# #Prints the board
# for w in word:
#     if w in correct_guesses:
#         print(w, end=' ')
#     else:
#         print('_', end=' ')
#
# #Allow 6 guesses
# while len(word) > len(correct_guesses) and num_turns < 5:
#     num_turns += 1 #count the turn
#
#     print()
#     print(num_turns)
#
#     print('You have already guessed', all_letters)
#
#     player_letter = input('\nGuess a letter')
#     #Don't let them repeat
#     while player_letter in all_letters:
#         print('You guessed that already!')
#         player_letter = input('\nGuess a letter:')
#
#     player_letter = player_letter.lower()
#     all_letters += (player_letter,)
#
#     #Check for correct answer
#     if player_letter in word:
#         print('Good guess!')
#         correct_guesses += (player_letter,) #saves correct answer
#
#     #Prints the board
#     for w in word:
#         if w in correct_guesses:
#             print(w, end=' ')
#         else:
#             print('_', end=' ')
#
# #tell them if they won or lost
# if len(word) > len(correct_guesses):
#     print('\nSorry you lost. The word was', word)
# else:
#     print('\nYou got it!')

#example
# file_handler = open('/Users/Jared Tsang/Desktop/harrypotter.txt', 'r')
# text = file_handler.read() #string
# text = text.lower()
#
# text = text.replace(',', '')
# text = text.replace(':', '')
# text = text.replace('.', '')
# text = text.replace('?', '')
# text = text.replace('(', '')
# text = text.replace(')', '')
# text = text.replace('"', '')
# text = text.replace('!', '')
# text = text.replace(';', '')
# text = text.replace('-', '')
#
# file_handler.close()
# tlist = text.split() #list
# ulist = list(set(tlist)) #uinque list
# ulist.sort()
# fo = open('/Users/Jared Tsang/Desktop/hp_wordcounts.txt', 'w')
# for w in ulist:
#     print(w, 'appears', tlist.count(w), file = fo)
# fo.close()
