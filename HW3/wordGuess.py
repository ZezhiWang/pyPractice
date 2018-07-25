# -*- coding: cp1252 -*-

# description: guess word

# name: Wang Zezhi

# date: Sep.27th 2015

import random

print "Try to guess the word I'm thinking of.\nIf the word you guess comes after my word in the dictionary,\nI will say 'too far.\nIf the word you guess comes before my word,\nI will say 'go farther'."

def wordguess():
    f=open('wordlist1000.txt','r')
    list0=[]

    for w in f:
        list0.append(w[:-1])
    f.close()

    result = list0[random.randint(0,999)]
    guess = "Q"
    counter = 1

    for counter in range (0,40):
        guess = raw_input("Enter your guess: ")
        if guess == "Q" :
            break
        else :
            if guess in list0:
                if list0.index(guess) < list0.index(result):
                    print "go further"
                elif list0.index(guess) > list0.index(result) :
                    print "too far"
                else :
                    print "You got it! It took you %d guesses." %counter
                    break
            else :
                print "Error, again"
    
    if list0.index(guess) != list0.index(result):
        print "You fail"

wordguess()
