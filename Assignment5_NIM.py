print "Assignment 5 : NIM"
print "Type 'play(int, int, int)' to start playing"
print

def legalMoves(board): # Determines all possible legal moves
    possibilities=[]
    for p in range(3):
        for t in range(board[p]):
            possibilities.append ((p,t+1))
    return possibilities

def newBoard(b,m):
    change = b[m[0]] - m[1]
    if m[0] == 0:
        board = (change,b[1],b[2]) # Changes board values by editing the tuple
    if m[0] == 1:
        board = (b[0],change,b[2])
    if m[0] == 2:
        board = (b[0],b[1],change)
    return board

def isLegalMove(board,move): # Checks if the player is inputting a legal move
    posMoves = legalMoves(board)
    for m in posMoves:
        if move[0] < 3 and board[move[0]] >= move[1] and move[1] > 0:
            return True
        else:
            return False

def binarySum(board): # Uses the binary sum formula to make winning moves
    s = board[0]^board[1]^board[2]
    binSum = bin(s)[2]
    c = 0
    for x in range(len(binSum)):
        if binSum[x] == '1':
            c += 1
        if c >= 1:
            return True
        else:
            return False

def canWin(board): # Uses binarySum to check if the player can still win
    posMoves = legalMoves(board)
    if binarySum(board):
        for m in posMoves:
            nextBoard = newBoard(board, m)
            if not binarySum(nextBoard):
                return m

def nextMove(board): #Finds best possible move and returns it, used to calculate computer's moves
    import random
    return canWin(board)
    n = posMove[random.randint(0,len(posMoves)-1)]
    return n

def play(row0,row1,row2): # Instantiates a game of NIM with user-inputted rows
    print 'The game is NIM'
    print
    board = (row0,row1,row2)
    player = 0
    while board != (0,0,0):
        for i in range(3):
            boardUI = str(i) + ': ' + 'I '*board[i]
            print boardUI
        if player == 0:
            while True: # Loops for player to take matches from a row
                rowSelect = raw_input('Choose a row: ')
                numSelect = raw_input('How many matches from row ' + rowSelect + '?: ')
                move = (int(rowSelect),int(numSelect))
                if move in legalMoves(board): # Tests if moves are valid
                    break
                else:
                    print 'Invalid move'
        else:
            move = nextMove(board)
            print 'Computer takes ' + str(move[1]) + ' from row ' + str(move[0]) + '.'
        board = newBoard(board,move)
        player = (player+1)%2
    if player == 1:
        print 'Wow...You won!'
    else:
        print 'I win!'
