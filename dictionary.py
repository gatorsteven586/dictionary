# glossary = {
#     'rabbit' : 'a small mamallian creature that hops and has long ears',
#     'chicken' : 'a small flightless bird that crosses roads',
#     'dog' : "a stinky animal that barks and poops and is generally annoying",
#     'cat' : 'a cunning, mysterious, and lazy animal that says "Meow!"',
#     'fish' : 'an animal that swims underwater and eats other fish'
#     }

# MY ATTEMPT AT SORTING AND ADDING NUMBERS. NEED TO LINK TO DEF SOMEHOW
# wordlist = []
# deflist = []
# for index, word in enumerate(sorted(glossary), start = 1):
#     print(f"{index}: \t {word.title()}")
#     wordlist.append(word)
#     deflist.append(glossary[word])

import json
from os import system, name 
filename = 'dictionary.json'

with open(filename) as f:
    glossary = json.load(f)
# stored = {}
# addfirst = input('First: ')
# addlast = input('Last: ')
# stored[addfirst] = addlast
# print(stored)


# CHOOSING
choice = 0
system('cls')
print('Welcome to the dictionary, where you can lookup or add your own words and definitions!')
print('Dont get too CRAZY!!')
while choice != 3:
    print('\nNow, what would you like to do...')
    print('\t[1]: Add a word?')
    print('\t[2]: Know a word?')
    print('\t[3]: Exit')
    choice = int(input('Enter your choice: '))
    system('cls')
    if choice == 1:
        addword = input('What is the word you would like to add? ')
        adddef = input('Ok great, what a cool word. What does it mean? ')
        print('Very cool, I will add that word to your dictionary')
        glossary[addword] = adddef
    elif choice == 2:
        print('Here is a list of words in the dictionary:')
        for word in sorted(glossary):
            print(f'\t {word.title()}')

        userinput = input('Which one do you want to know about? ')

        # print("\nHere's your definition, you filthy animal:")
        system('cls')
        print(f"A {userinput}! You would like to know what a {userinput} is? \nIt is {glossary[userinput]}.")
        print('\nThere! Are you happy??\n')
        print('---------------------------------------------')
print('Alright, see you later you filthy animal!')
print("Remember: Dont step on a crack or you'll break Penny's back!")
with open(filename, 'w') as f:
    json.dump(glossary, f)

# print('Here are your words...defined!')
# for word, definition in glossary.items():
#     print(f"\tYou would like to know what a {word.title()} is? \n\t\tIt is {definition}.")
# print('Now you know so many words!')
# print('CHICKENNNNNNN!')

# print('These are the words:')
# for word in glossary.keys():
#     print(f"\t {word}")

# print('\nThese are the definitions:')
# for definition in glossary.values():
#     print(f'\t {definition}')