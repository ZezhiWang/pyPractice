#The eight queens puzzle.
#The board size can be > 8 

#The recursive function for solving the puzzle will be created in
#stages  The argument to the function is a partially solved puzzle,
#which is given by specifying the board size, and a tuple giving the
#positions in the filled rows.

#For example, if the tuple is (1,4,2) then there is a queen on column 1
#of row 0, on column 4 of row 1, and on column 2 of row 2.  The board size
#in this example must be at least 5, but it could be larger.

#Safety of a position (whether two queens are attacking one another) depends
#only on the tuple, and not on the board size.

"""The following function starts with a partially filled board (a tuple) that
is assumed to be safe and determines whether placing a queen on the next column
for the given row is safe. Returns True if the move is safe, False otherwise. """
def isSafe(board, row):
    # if there is another column that has a Queen
    # on the same row... then we can quickly determine its not safe
    if row in board:  
        return False

    # now lets check the diagonals 
    for col in range(len(board)):
        if row-board[col]==len(board)-col:
            return False
        if row-board[col]==col-len(board):
            return False
    return True

""" This is the main function. It returns the first solution it finds,
 and returns nothing (return value None) if no solution is found.
 This is how we back out of the recursion as soon as a solution is
 encountered. """

def eightqueens(size,board):
    if size > len(board): # General Case
        for j in range(size): # check each row 
            if isSafe(board,j): # would it be safe to place a Queen at row index j ?
                newBoard=board+(j,) # since its a safe move, create newboard
                result = eightqueens(size,newBoard) # recursively call function 
                if result != None:
                    return result 
                
    else: # Base Case : len(board) == 8,
          # hence we are done... board completetly filled
        return board

""" test function call .. only if not using gui"""
def test():
    eightqueens(8,tuple())

""" This function is used by the GUI. It creates updates a list of the
    boards examined (including unsafe
    ones). This will be used for animated display."""
def eightqueensList(size,board,transcript):
    if size>len(board):
        for j in range(size):
 
            if isSafe(board,j):
                newBoard=board+(j,)
                transcript.append(board+(j,))
                result = eightqueensList(size,newBoard,transcript)
                if result != None:
                    return result
    else:
        return board
    
""" This function is used by the GUI """
def testList(size):
    transcript=[]
    eightqueensList(size,tuple(),transcript)
    return transcript
