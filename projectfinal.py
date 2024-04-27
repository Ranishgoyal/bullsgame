import pyttsx3
import random

def getDigits(num):
    return [int(i) for i in str(num)]

def noDuplicates(num):
    num_li = getDigits(num)
    return len(num_li) == len(set(num_li))

def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num

def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i, j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

num = generateNum()
tries = int(input('Enter number of tries: '))
speak("Welcome to the guessing game. You have {} tries to guess the 4-digit number.".format(tries))

while tries > 0:
    guess = int(input("Enter your guess: "))
    
    if not noDuplicates(guess):
        speak("Number should not have repeated digits. Please try again.")
        continue
    if guess < 1000 or guess > 9999:
        speak("Please enter a 4-digit number only.")
        continue
    
    bull_cow = numOfBullsCows(num, guess)
    speak("{0} correct and {1} correct but on wrong place.".format(bull_cow[0], bull_cow[1]))
    tries -= 1
    
    if bull_cow[0] == 4:
        speak("Congratulations! You guessed the correct number.")
        break
    elif tries == 0:
        speak("You ran out of tries. The number was {}.".format(num))
    else:
        speak("You have {} tries left.".format(tries))