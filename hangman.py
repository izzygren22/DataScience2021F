# Hangman Game
    
wordList = ['cherry', 'apple', 'watermelon']


def getHdnWord(word):
    hdnWord = []
    for x in word: 
        hdnWord.append('*')
    return hdnWord

def checkGuess(word, guessNum, hdnWord):
    guess = input('Enter Guess: ')
    guessNum -= 1
    if guess in word: # if guess correct
        print('Correct!')
        changeWord(hdnWord, guess, word)
    else:
        print('Wrong!')
        print(' '.join(hdnWord))
    
    guesstxt = 'You have {} guesses left!'
    print(guesstxt.format(guessNum))

def changeWord(hdnWord, guess, word):
    for i in range(len(word)):
        if word[i] == guess:
            hdnWord[i] = guess
    print(' '.join(hdnWord))
 

def runGame():
    #move to startgame() later
    word = [ 'a', 'p', 'p', 'l', 'e']
    guessNum = 10
    hdnWord = getHdnWord(word)
    # end startgame()
    
    while '*' in hdnWord or guessNum < 0:
        checkGuess(word, guessNum, hdnWord)
    print('Game Over!')

runGame() 
    
# TO DO:
    #GUESSNUM NOT WORKING
    # Enter Guess: 
    #check answer()
    #choose word()
    #start game()
    #end message()
    