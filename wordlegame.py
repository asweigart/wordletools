"""Wordle Game Clone by Al Sweigart al@inventwithpython.com
"""

import random, sys

def getClue(guessWord, secretWord):
    """getClue() returns the string to display to the user that has the
    clues about which letters in guessWord exist in secretWord."""
    clue = ''
    for i in range(5):  # Go over each of the 5 letters.
        if guessWord[i] == secretWord[i]:
            # The letter at guessWord[i] is in the correct spot.
            clue = clue + '|' + guessWord[i] + '|'
        elif guessWord[i] in secretWord:
            # The letter at guessWord[i] is in the secret word but at
            # a different spot.
            clue = clue + '.' + guessWord[i] + '.'
        else:
            # The letter at guessWord[i] is not in the secret word.
            clue = clue + ' ' + guessWord[i] + ' '
    return clue


# Start of the program.
print('Wordle Game Clone by Al Sweigart al@inventwithpython.com')
print()
print('Guess the WORDLE in six tries.')
print('Each guess must be a valid five-letter word.')
print('After each guess, the marking around the letters will change to')
print('show how close your guess was to the word.')
print()
print('Examples:')
print('|W| E  A  R  Y')
print('The letter W is in the word and in the correct spot.')
print()
print(' P .I. L  L  S')
print('The letter I is in the word but in the wrong spot.')
print()
print(' V  A  G  U  E')
print('The letters V, A, G, U, and E are not in the word in any spot.')
print()

# Read in the secret words from list-of-possible-solution-words.txt:
allSecretWords = []
with open('list-of-possible-solution-words.txt') as fileObj:
    for line in fileObj.readlines():
        allSecretWords.append(line.strip())

# Read in the valid guess words from list-of-valid-guess-words.txt:
allGuessWords = []
with open('list-of-valid-guess-words.txt') as fileObj:
    for line in fileObj.readlines():
        allGuessWords.append(line.strip())

# Pick a secret word:
secretWord = random.choice(allSecretWords)

guessNumber = 1  # Start a guess #1
while guessNumber <= 6:
    while True:
        # Keep looping until the user enters a valid guess.
        print('#' + str(guessNumber) + ' Guess a five-letter word:')
        guess = input('> ')
        guess = guess.upper()  # Convert guess to uppercase.
        if len(guess) != 5:
            print('Your guess must be a 5-letter word.')
            continue
        if guess not in allGuessWords:
            print(guess + ' is not a valid word.')
            continue
        break

    print(getClue(guess, secretWord))

    if guess == secretWord:
        print('Correct! You have won.')
        sys.exit()
    else:
        guessNumber = guessNumber + 1

print('The secret word was: ' + secretWord)
