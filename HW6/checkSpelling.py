# HW #6 - Problem 1

def ED(first, second):
   m = len(first) + 1
   n = len(second) + 1
   dist = {}
   for i in range(m):
      dist[i,0] = i
   for j in range(n):
      dist[0,j] = j
   for i in range(1, m):
      for j in range(1, n):
         cost = 0 if first[i-1] == second[j-1] else 1
         dist[i,j] = min(dist[i, j-1]+1, dist[i-1, j]+1, dist[i-1, j-1]+cost)
   return dist[m - 1, n - 1]

def ED0(first,second):
   if len(first) == 0:
      return len(second)
   elif len(second) == 0:
      return len(first):
   elif first[0] == second[0]:
      return ED(first[1:], second[1:])
   else:
      x = ED(first, second[1:])
      y = ED(first[1:], second)
      z = ED(first[1:], second[1:])
      return 1 + min(x, y, z)

def loadFile(filename):
   File = open(filename,'r')
   wordList=[words.strip() for words in File]
   File.close()
   return wordList

def spellChecker() :
   wordList = loadFile('wordlist.txt')
   word = raw_input("Please input your word: ")
   if word in wordList:
      print "Correct Spelling"
   else:
      result = []
      counter = 1
      while len(result) < 5:
         result += [(counter, item) for item in wordList if ED(word, item) == counter]
         counter += 1
      print result[:5]
   
   command = raw_input("Enter 'quit' to exit or enter anything to Try Again: ")
   if command != "quit":
      spellChecker()

spellChecker()