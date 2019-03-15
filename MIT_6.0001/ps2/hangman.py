# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
Vowels = 'aeiou'


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for l in secret_word:
        if l not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ''
    for l in secret_word:
        if l in letters_guessed:
            result += l
        else:
            result += '_ '
    return result



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ''
    for s in string.ascii_lowercase:
        if s not in letters_guessed:
            result += s
    return result
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_warnings = 3
    #secret_word = 'tact'
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    print("You have {} warnings left.".format(num_warnings))
    #print("-------------")
    
    num_guesses = 6
    win = False
    letters_guessed = []
    g_w = get_guessed_word(secret_word, letters_guessed)
    
    while not win and num_guesses > 0 and num_warnings >= 0:
        print("-------------")
        print("You have {} guesses left.".format(num_guesses))
        
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {}".format(available_letters))
        
        
        g = input("Please guess a letter:")
        if not str.isalpha(g) :
            num_warnings -= 1
            print("Oops! That is not a valid letter. You have {} warnings left: ".format(num_warnings),end='')
            print(g_w)
        elif g not in available_letters:
            print("Oops! You've already guessed that letter.", end='')
            if num_warnings > 0:
                num_warnings -= 1
                print("You have {} warnings left:".format(num_warnings),end='')
            else:
                print("You have no warnings left, so you lose one guess:",end='')
                num_guesses -= 1
            print(g_w)
        else:
            # transform into lowercase
            g = str.lower(g)
            letters_guessed.append(g)
            g_w = get_guessed_word(secret_word, letters_guessed)
        
        
            if g in secret_word:
                # the user loses  no  guesses.
                print("Good guess: {}".format(g_w))
            elif g in Vowels:
                #If the vowel hasn’t been guessed and the vowel is not in the secret
                #word, the user loses  two  guesses. 
                #Vowels are  a,  e,  i,  o, and  u.  y does not count as a vowel.
                print("Oops! That letter is not in my word: {}".format(g_w))
                num_guesses -= 2
            else:
                print("Oops! That letter is not in my word: {}".format(g_w))
                num_guesses -= 1
                
        # check whether the player has won the game
        if is_word_guessed(secret_word, letters_guessed):
            win = True
            break

    
    print("-------------")
    if not win:
        print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))
    else:
        print("Congratulations, you won!")
        total_score = num_guesses * len(set(secret_word))
        print("Your total score for this game is: {}".format(total_score))
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    def strip_space(my_word):
        return my_word.replace(" ", "")
    
    def calculate_length(my_word):
        return len(strip_space(my_word))
    
    def strip_underscore(my_word):
        return my_word.replace(" ", "").replace("_", "")
    
    
    if calculate_length(my_word) != len(other_word.strip()):
        return False
    else:
        my_word = strip_space(my_word)
        for i in range(len(my_word)):
            if my_word[i] != '_':
                if my_word[i] != other_word[i]:
                    return False
            elif other_word[i] in my_word:
                return False
            else:
                continue
            
    return True
#        characters = strip_underscore(my_word)
#        # determine wheter my_word is a proper subset of other_word
#        return set(characters) < set(other_word)
            
        
    
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = [word for word in wordlist if match_with_gaps(my_word, word)]
    if len(result) > 0:
        print(" ".join(result)) 
    else:
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_warnings = 3
    #secret_word = 'tact'
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
    print("You have {} warnings left.".format(num_warnings))
    #print("-------------")
    
    num_guesses = 6
    win = False
    letters_guessed = []
    g_w = get_guessed_word(secret_word, letters_guessed)
    
    while not win and num_guesses > 0 and num_warnings >= 0:
        print("-------------")
        print("You have {} guesses left.".format(num_guesses))
        
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {}".format(available_letters))
        
        
        g = input("Please guess a letter:")
        if g is "*":
            print("Possible word matches are:")
            show_possible_matches(g_w)
            continue
        
        
        if not str.isalpha(g) :
            num_warnings -= 1
            print("Oops! That is not a valid letter. You have {} warnings left: ".format(num_warnings),end='')
            print(g_w)
        elif g not in available_letters:
            print("Oops! You've already guessed that letter.", end='')
            if num_warnings > 0:
                num_warnings -= 1
                print("You have {} warnings left:".format(num_warnings),end='')
            else:
                print("You have no warnings left, so you lose one guess:",end='')
                num_guesses -= 1
            print(g_w)
        else:
            # transform into lowercase
            g = str.lower(g)
            letters_guessed.append(g)
            g_w = get_guessed_word(secret_word, letters_guessed)
        
        
            if g in secret_word:
                # the user loses  no  guesses.
                print("Good guess: {}".format(g_w))
            elif g in Vowels:
                #If the vowel hasn’t been guessed and the vowel is not in the secret
                #word, the user loses  two  guesses. 
                #Vowels are  a,  e,  i,  o, and  u.  y does not count as a vowel.
                print("Oops! That letter is not in my word: {}".format(g_w))
                num_guesses -= 2
            else:
                print("Oops! That letter is not in my word: {}".format(g_w))
                num_guesses -= 1
                
        # check whether the player has won the game
        if is_word_guessed(secret_word, letters_guessed):
            win = True
            break

    
    print("-------------")
    if not win:
        print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))
    else:
        print("Congratulations, you won!")
        total_score = num_guesses * len(set(secret_word))
        print("Your total score for this game is: {}".format(total_score))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
