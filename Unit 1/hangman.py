import random


def getWord():
    wordList = ['cherry', 'apple', 'watermelon']
    word = random.choice(wordList)  # get random word from list
    return word


def startGame(word):
    theme = 'fruits'
    print('Welcome to Hangman!')
    srtTxt = ('The secret word has {} letters and the theme is ' + theme)
    print(srtTxt.format(len(word)))


def getHdnWord(word):
    hdnWord = []
    for x in word:  # loop word list
        hdnWord.append('*')
    return hdnWord


def checkGuess(word, guesses, hdnWord):
    guess = input('Enter Guess: ')
    guesses.append(guess)  # add guess to guesses list
    if guess in word:  # if guess correct
        print('Yes, "' + guess + '" is in the word :)')
        changeWord(hdnWord, guess, word)
    else:
        print('Nope! :(')
        print(' '.join(hdnWord))  # print hdnWord as string


def getGuessInfo(guesses):
    print('So far you have guessed:')
    print(', '.join(guesses))  # print guesses as string with commas
    guessTxt = 'You have {} guesses left!'
    guessNum = 10 - (len(guesses))  # 10 - number of guesses
    print(guessTxt.format(guessNum))


def changeWord(hdnWord, guess, word):
    # change the * to the guessed letter in hdnWord
    for i in range(len(word)):
        if word[i] == guess:
            hdnWord[i] = guess
    print(' '.join(hdnWord))  # print hdnWord as string


def runGame():
    word = getWord()
    hdnWord = getHdnWord(word)
    guesses = []

    startGame(word)

    # while word not guessed & have guessed less than 10 times
    while '*' in hdnWord and len(guesses) < 10:
        checkGuess(word, guesses, hdnWord)
        getGuessInfo(guesses)
    print('Game Over :)')


runGame()
