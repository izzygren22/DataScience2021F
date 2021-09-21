# Hangman Game
    
wordList = ['cherry', 'apple', 'watermelon']
gameEnd = False
word = [ 'a', 'p', 'p', 'l', 'e']
guess = input('Enter Guess: ')
guessNum = 10;

def getHdnWord(word):
    hdnWord = []
    for x in word: 
        hdnWord.append('*')
    #print(' '.join(hdnWord)) #print hidden word as string
    return hdnWord

    

def checkGuess(word, guess, guessNum):
    guessNum -= 1
    if guess in word: # if guess correct
        print('Correct!')
        guess
        changeWord(getHdnWord(word), guess, word)
    guesstxt = 'You have {} guesses left!'
    print(guesstxt.format(guessNum))
    
    


def changeWord(hdnWord, guess, word):
    for i in range(len(word)):
        if word[i] == guess:
            hdnWord[i] = guess
    print(' '.join(hdnWord))
            
#def runGame():
   # while gameEnd == False:
        ##startGame();
        #checkGuess(word,guess,guessNum);
    ##EndMessage();
    

    
    
checkGuess(word, guess, guessNum)
#def runGame():
    #while gameEnd = False:
        #startGame();
        #checkGuess();
    #EndMessage();

# TO DO:
    #check answer()
    #choose word()
    #end message()
    