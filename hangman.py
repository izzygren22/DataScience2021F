# Hangman Game

#def runGame():
    #while gameEnd = False:
        #startGame();
        #checkGuess();
    #EndMessage();
    
wordList = ['cherry', 'apple', 'watermelon']
guesses = 10
gameEnd = False
word = [ 'a', 'p', 'p', 'l', 'e']
guess = input('Enter Guess: ')
hdnWord = []

def getHdnWord():
    for x in word:
        hdnWord.append('*')
    print(hdnWord)
    

def checkGuess():
    guesses -= 1
    if guess in word:
        print('Correct')


def changeWord(word, guess):
    for guess in word:
        pass
        
getHdnWord()
#checkGuess()
#changeWord()