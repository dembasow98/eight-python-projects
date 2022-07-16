import random
from words import words
import string

def valid_word(words_list):
    word = random.choice(words) #choose a rondom word from the words list
    while '-' in word or ' ' in word: #if the random word contains '_' or ' ' characters(is invalid), choose another word
        word = random.choice(words_list)
    #return valid word(we'll make all the letter's upper)
    return word.upper()

def hangman():
    #Wrong letters:
    false_attempts = 7

    word = valid_word(words)
    #Get all the letters of the word:
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) #get all the alphabet letters in uppercase
    used_letters = set() #contains the already guessed letter of the word to be completed

    while len(word_letters) > 0:
        #if the man is hangued:
        if false_attempts == 0:
            print('Sorry, your MAN has been HANGUED!')
            break
        #print the used_letters if not null:
        if len(used_letters) > 0:
            print('Used letters: ', ' '.join(used_letters))
        
        #the current word status of completion:(ie: W-RD)
        word_letters_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word status: ',' '.join(word_letters_list))
        print(f'False attempts left: {false_attempts}')

        guessed_letter = input('Guess a letter: ').upper()
        if guessed_letter in alphabet - used_letters: #if the user guess letter is not used
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
            #if the used guess is not in the word:
            else:
                false_attempts -= 1
        elif guessed_letter in used_letters: #if the user guess letter is already used
            print('You have already used this letter!!!')
        else: #if the user input is an invalid character
            print('Invalid character!!!')

    #if the all the word letters are guessed correctly
    if(len(word_letters) == 0):
        print('Current word status: ',' '.join(word_letters_list))
        print(f"Congrats! You've guessed all the letters of the word {word.upper()} correctly!")

#Run the game here:


print('******************WELCOME TO HANGMAN GAME:*********************')
hangman()
choice = ''
while choice.lower() != 'n':
    choice = input('Do you want to play again? yes(y) or no(n): ')
    if choice.lower() == 'y':
        hangman()
    else:
        print('******************GAME OVER**********************')
