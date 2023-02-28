"""Letter alternative to Bagels from the bigbook of small
python projects"""

import random

NUM_LETTERS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-letter string with no repeated letters.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One letter is correct but in the wrong position.
  Fermi        One letter is correct and in the right position.
  Bagels       No letter is correct.

For example, if the secret string was abc and your guess was agb, the
clues would be Fermi Pico.'''.format(NUM_LETTERS))

    while True: # Main Game Loop
        #This stores the secret number the player needs to guess:
        secretString = getSecretString()
        print('I have thought up a string.')
        print(' You have {} guesses to get it'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_LETTERS or not guess.isalpha():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretString)
            print(clues)
            numGuesses += 1

            if guess == secretString:
                break  # They're correct so break the loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretString))

        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretString():
    """Returns a string made up of NUM_LETTERS unique random LETTERS."""
    characters = list('abcdefghijklmnopqrstuvwxyz') # Create a list of LETTERS a to z.
    random.shuffle(characters)

    # Get the first NUM_LETTERS letter in the list for your secret number:
    secretString = ''
    for i in range(NUM_LETTERS):
        secretString += str(characters[i])
    return secretString

def getClues(guess, secretString):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretString:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretString[i]:
            # A correct letter is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretString:
            # A correct letter is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct letters at all.
    else:
        #Sorts the clues into alphabetical order so their original order
        #doesn't give information away.
        clues.sort()
        #Make a single string from the list of string clues.
        return ' '.join(clues)

#If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
