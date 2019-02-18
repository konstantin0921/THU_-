# Tic Tac Toe game in python
import copy

# stores Xs and Os, player can make a move by inserting in position 1-9
board = [' ' for x in range(10)]
#board = [' ', 'X', 'O', 'O', 'X', ' ', 'O', ' ', ' ', 'X']
COMP = 'O'
HUMAN = 'X'


def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard():
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def game_over(board):
    return isWinner(board, 'O') or isWinner(board, 'X')

def playerMove():
    run = True
    while run:
        try:
            move = input('''Please select a position to place an X (1-9): ''')
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)

                else:
                     print("you can not put it there, try again")
                     continue
            else:
                print('Please type a number within the range')
                continue
        except:
            print('Please type a number')
            continue



def minimax(board, depth, player):
    if player == COMP:
        best = [-1, float('-inf')]
    else:
        best = [-1, float('inf')]

    if depth == 0 or game_over(board):
        # no empty cell or game over

        score = evaluate(board)
        return [-1, score]

    for cell in empty_cells(board):
        # pretending to choose one cell
        if player == COMP:
            boardCopy = board[:]
            boardCopy[cell] = 'O'
            score = minimax(boardCopy, depth-1, HUMAN)
            score[0] = cell
        else:
            # Human

            boardCopy = board[:]
            boardCopy[cell] = 'X'
            score = minimax(boardCopy, depth-1, COMP)
            score[0] = cell

        if player == COMP:
            if score[1] > best[1]:
                best = score
        else:
            if score[1] < best[1]:
                best = score

    return best


def compMove():
    depth = len(empty_cells(board))

    move = minimax(board, depth, COMP)
    return move[0]

def evaluate(board):
    if isWinner(board, 'O'):
        # if computer is the winner
        score = 1
    elif isWinner(board, 'X'):
        score = -1
    else:
        score = 0
    return score

def empty_cells(board):
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    return possibleMoves

def selectRandom(li):
    import random
    return random.choice(li)

def isBoardFull(board):
    return all([board[i]!=' ' for i in range(1, 10)])

def main():
    #Main game loop, we assume that Player always plays first
    #Player is X, computer is O
    print('''Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical). The board has positions 1-9 starting at the top left.''')
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            #print('Sorry, Computer[O] has won')
            break

        if not(isWinner(board, 'X')):
            print('Computer turn...')
            move = compMove()
            if move == -1:
                # the board is full, tie game
                break
            else:
                insertLetter('O', move)
                print('Computer placed an O in position ', move)
                printBoard()
        else:
            #print('Congratulations, you have won')
            break


    if isWinner(board, 'O'):
        print('Sorry, Computer[O] has won')
    elif isWinner(board, 'X'):
        print('Congratulations, you have won')
    else:
        print('Tie Game!')



if __name__ == '__main__':
    main()
