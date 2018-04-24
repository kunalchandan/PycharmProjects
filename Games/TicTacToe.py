import numpy as np


def gameFinished(game):
    done = True
    for x in range(len(game)):
        for y in range(len(game[x])):
            if game[x][y] == 0:
                done = False
    return done

def gameWon(game):
    for each in range(len(game)):
        if np.array_equal(game[each], np.zeros(len(game)) + 1):
            return 'Player 1'
        if np.array_equal(game[each], np.zeros(len(game)) + 2):
            return 'Player 2'
        if np.array_equal(game[:, each], np.zeros(len(game)) + 1):
            return 'Player 1'
        if np.array_equal(game[:, each], np.zeros(len(game)) + 2):
            return 'Player 2'
    # Check Diagonals
    if np.array_equal(np.diag(game), np.zeros(len(game)) + 1):
        return 'Player 1'
    if np.array_equal(np.diag(np.fliplr(game)), np.zeros(len(game)) + 2):
        return 'Player 2'
    return True


board = np.zeros((3, 3), int)

count = 0
while (gameFinished(board) is False) and (gameWon(board) is True):
    count %= 2
    count += 1
    print(board)
    move = int(input('Player ' + str(count) + '\'s turn\n'))
    if board[int(move / len(board))][move % len(board)] == 0:
        board[int(move / len(board))][move % len(board)] = count
    else:
        print(board)
        print('You can\'t move there, pick again. This is your last try otherwise you lose!')
        move = int(input('Player ' + str(count) + '\'s turn\n'))
        if board[int(move / len(board))][move % len(board)] == 0:
            board[int(move / len(board))][move % len(board)] = count

print(gameWon(board))