import numpy as np

# Tests if all the squares are filled
def gameFinished(game):
    done = True
    for x in range(len(game)):
        for y in range(len(game[x])):
            if game[x][y] == 0:
                done = False
    return done

# Tests who won the game
def gameWon(game):
    for each in range(len(game)):
	# Tests by checking lengths of arrays instead of the use of loops.
	# It made the logic slightly easier.
        if np.array_equal(game[each], np.zeros(len(game)) + 1):
            return 'Player 1 Wins'
        if np.array_equal(game[each], np.zeros(len(game)) + 2):
            return 'Player 2 Wins'
        if np.array_equal(game[:, each], np.zeros(len(game)) + 1):
            return 'Player 1 Wins'
        if np.array_equal(game[:, each], np.zeros(len(game)) + 2):
            return 'Player 2 Wins'
    # Check Diagonals
    if np.array_equal(np.diag(game), np.zeros(len(game)) + 1):
        return 'Player 1 Wins'
    if np.array_equal(np.diag(np.fliplr(game)), np.zeros(len(game)) + 2):
        return 'Player 2 Wins'
    return True


board = np.zeros((3, 3), int)

count = 0
while (gameFinished(board) is False) and (gameWon(board) is True):
    count %= 2
    count += 1
    pickFailed = False
    print(board)
    move = int(input('Player ' + str(count) + '\'s turn\n'))
    #Check if the attempted location is clear
    if board[int(move / len(board))][move % len(board)] == 0:
        board[int(move / len(board))][move % len(board)] = count
    else: # Otherwise fail pick and enter loop
        pickFailed = True
    # This is only necessary since Python doesn't have do-while loops
    while pickFailed:
        print(board)
        print('You can\'t move there, pick again.')
        move = int(input('Player ' + str(count) + '\'s turn\n'))
        if board[int(move / len(board))][move % len(board)] == 0:
            board[int(move / len(board))][move % len(board)] = count
	    pickFailed = False
		

print(gameWon(board))
