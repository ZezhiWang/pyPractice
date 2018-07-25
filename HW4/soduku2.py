
# Description: The Sudoku puzzle
# Name:Wang Zezhi
# Date:Oct.15th

import random
import os
import os.path
import time
t0 = time.time()

def gridDisplay(board):
    for j in range(9):
        for k in range(9):
            print board[j][k],
            if k%3==2:
                print ' ',
        print 
        if j%3 == 2:
            print ""

""" Test the routines for determining safety and placement.
This randomly generates a sequence of n characters to
successively test and place in an initially empty grid/board. """
def testGrid():
   board=((0,)*9,)*9 # create a board with all zeros
   gridDisplay(board) # display board
   for trial in range(10):
        row = random.randint(0,8)
        col = random.randint(0,8)
        x = random.randint(1,9) # randomly choose digit to place at row and col
        print 'place ', x , 'at row ', row+1, ' column ', col+1
        if board[row][col] != 0:
            print 'OCCUPIED'
        elif isSafe(board,row,col,x):
            print 'SAFE'
            board = place(board,row,col,x)
            print
            gridDisplay(board)
        else:
            print 'UNSAFE'
   gridDisplay(board)

""" Set the board based on content (as read from an input file)."""
def setBoard(content):
   board = ()
   i = 0
   for line in content:
      currentRow = ()
      j = 0
      for num in line:
         if(num != ' ' and not ('\n' in num or '\r' in num)):
            currentRow =  currentRow  + (int(num),)
            j += 1
      board = board + (currentRow,)
      i += 1
   return board
   
def loadFile(fileName):
    if(fileName != ''):
      # Opens the selected file
      file_in = open(fileName, 'r')
      # Now read the file and load the board as appropriate.
      lines = file_in.readlines()
      print('load_file: lines = ', lines)
      board = setBoard(lines)
      (_, name) = os.path.split(fileName)
      file_in.close()
      return board 
 
########################################################################################
# Complete following functions
########################################################################################
""" A function that returns True if adding the digit X to the given
row and column of a puzzle board results in a safe board, otherwise,
it returns false."""
def isSafe(board, row, column, x):
   temp = place ( board, row, column, x)
   if rowCheck(temp, row) and columCheck(temp, column) and clusterCheck(temp, row, column) :
       return True
   return False

""" Checks a given column for a valid set of numbers"""
def columCheck(board, column):
   # TODO
   Col = tuple()
   for i in range(0,9):
       Col = Col + (board[i][column],)
   for j in Col :
       if Col.count(j) > 1 and j != 0 :
           return False
   return True
   print "PLACE HOLDER FOR columCheck"
    
""" Checks a given row for a valid set of numbers"""
def rowCheck(board, row):
   # TODO
   Row = board[row]
   for i in Row :
       if Row.count(i) > 1 and i != 0 :
           return False
   return True
   print "PLACE HOLDER FOR rowCheck"
     
""" Checks cluster for a valid set of numbers, given row and column """
def clusterCheck(board, row, column):
   # TODO
   row = row/3
   col = column/3
   Cluster = tuple()
   for i in range(row*3,row*3+3):
       for j in range(col*3,col*3+3):
           Cluster = Cluster + (board[i][j],)
   for n in Cluster :
       if Cluster.count(n) > 1 and n != 0 :
           return False
   return True
   print "PLACE HOLDER FOR clusterCheck"
            
""" A function that updates the given puzzle board. It places
the element x at given row and column, and return the new board. """
def place(board, row, column, x):
   # 1st update row to contain x
   currentRow = board[row]
   currentRow = currentRow[0:column] + (x,) + currentRow[column+1:]
   # 2nd update whole puzzle board (board) to have updated row
   board = board[:row] + (currentRow,) + board[row+1:]
   return board

""" A function that return a tuple (row,col) which represents the row
and column of an empty cell (one that has the value zero). If no such
cell exists (which means the puzzle is solved), return None """
def firstEmpty(board) :
   # TODO
   result = tuple()
   for i in range(0,9):
      for j in range(0,9):
         if board[i][j] == 0 :
            result = result + (i,) + (j,)
            break
   print result
   return result
                                                            
""" Call this function to solve the sudoku board.
It should call the recursive function solveHelper  """
def sudokuSolve(board) :
   # TODO
   temp = firstEmpty(board)
   row = temp[0]
   col = temp[1]
   result = solveHelper(board,row,col)
   print "PLACE HOLDER FOR sudokuSolve"
   if result != None:
       gridDisplay(result)
   t1 = time.time()
   print t1 - t0

""" Solve the puzzle using recursion and backtracking """
def solveHelper(board, row, col):
   # TODO
    for i in range(1,10):
        if isSafe(board, row, col, i):
            newboard = place(board, row, col, i)
            new = firstEmpty(newboard)
            if len(new) == 0:
                return newboard
            else:
                newrow = new[0]
                newcol = new[1]
                result = solveHelper(newboard,newrow,newcol)
                if result != None:
                    return result


   
#___MAIN___
# TODO update file path accordingly 
board = loadFile(os.getcwd()+"\\extreme.txt")
print "*** BOARD INITAL CONFIGURATION ***"
gridDisplay(board)

sudokuSolve(board)
