# a hangman game that allows the user to guess letters in the randomly selected word

import random 

word_list = ['orange','intelligent', 'morning', 'haunt', 'detailed', 
'rude', 'right', 'curious', 'pause', 'carry', 'code', 'python']

random.shuffle(word_list)
answer = list(word_list[0])
display = []
used = []
display.extend(answer)
used.extend(display)

for i in range (len(display)):
    display[i] = "_"

print(' '.join(display))
print()

count = 0

print("This is hangman. I'm thinking of a word, Lets see if you can guess it")

while count < len(answer):
    guess = input("Pick a letter that you think the word contains: ")
    guess = guess.lower()
    print()
    # print(count)

    for i in range(len(answer)):
        if answer[i] == guess and guess in used:
            display[i] = guess
            count = count + 1

            used.remove(guess)

# if letter is not in the selected word 
    if guess not in display:
        print("Sorry, doesnt contain that one")

    print("You have guessed:",count,"letters correctly.")
    print()

    print(' '.join(display))
    print()

print("Cool, You guessed the word!")