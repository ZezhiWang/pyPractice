#supporting code for one of the homework assignments--
#returns a randomly chosen word from a list of the
#1000 (actually 999, for some reason) English words


import random

def randomword():
    f=open('wordlist1000.txt','r')
    wordlist=[]
    for w in f:
        wordlist.append(w[:-1])
    f.close()
    return wordlist[random.randint(0,999)]
