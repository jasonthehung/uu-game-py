from copy import deepcopy

def printBoard(board):
    print(board[0] + "(00)----------------------" + board[1] +
          "(01)----------------------" + board[2] + "(02)")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|       " + board[8] + "(08)--------------" +
          board[9] + "(09)--------------" + board[10] + "(10)  |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |        " + board[16] + "(16)-----" +
          board[17] + "(17)---" + board[18] + "(18)      |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print(board[3] + "(03)---" + board[11] + "(11)--" + board[19] + "(19)              " +board[20] + "(20)-----" + board[12] + "(12)--" + board[4] + "(04)")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |         |                   |          |      |")
    print("|       |        " + board[21] + "(21)-----" +
          board[22] + "(22)---" + board[23] + "(23)      |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       |                   |                    |      |")
    print("|       " + board[13] + "(13)--------------" +
          board[14] + "(14)--------------" + board[15] + "(15)  |")
    print("|                           |                           |")
    print("|                           |                           |")
    print("|                           |                           |")
    print(board[5] + "(05)----------------------" + board[6] +
          "(06)----------------------" + board[7] + "(07)")
    print("\n")




def adjacentLocations(position):
    adjacent = [
        [1, 3],
        [0, 2, 9],
        [1, 4],
        [0, 5, 11],
        [2, 7, 12],
        [3, 6],
        [5, 7, 14],
        [4, 6],
        [9, 11],
        [1, 8, 10, 17],
        [9, 12],
        [3, 8, 13, 19],
        [4, 10, 15, 20],
        [11, 14],
        [6, 13, 15, 22],
        [12, 14],
        [17, 19],
        [9, 16, 18],
        [17, 20],
        [11, 16, 21],
        [12, 18, 23],
        [19, 22],
        [21, 23, 14],
        [20, 22]
    ]
    return adjacent[position]

def isPlayer(player, board, p1, p2):
    if (board[p1] == player and board[p2] == player):
        return True
    else:
        return False


# Function to check if a player can make a mill in the next move.
# Return True if the player can create a mill
def checkNextMill(position, board, player):
    mill = [
        (isPlayer(player, board, 1, 2) or isPlayer(player, board, 3, 5)),
        (isPlayer(player, board, 0, 2) or isPlayer(player, board, 9, 17)),
        (isPlayer(player, board, 0, 1) or isPlayer(player, board, 4, 7)),
        (isPlayer(player, board, 0, 5) or isPlayer(player, board, 11, 19)),
        (isPlayer(player, board, 2, 7) or isPlayer(player, board, 12, 20)),
        (isPlayer(player, board, 0, 3) or isPlayer(player, board, 6, 7)),
        (isPlayer(player, board, 5, 7) or isPlayer(player, board, 14, 22)),
        (isPlayer(player, board, 2, 4) or isPlayer(player, board, 5, 6)),
        (isPlayer(player, board, 9, 10) or isPlayer(player, board, 11, 13)),
        (isPlayer(player, board, 8, 10) or isPlayer(player, board, 1, 17)),
        (isPlayer(player, board, 8, 9) or isPlayer(player, board, 12, 15)),
        (isPlayer(player, board, 3, 19) or isPlayer(player, board, 8, 13)),
        (isPlayer(player, board, 20, 4) or isPlayer(player, board, 10, 15)),
        (isPlayer(player, board, 8, 11) or isPlayer(player, board, 14, 15)),
        (isPlayer(player, board, 13, 15) or isPlayer(player, board, 6, 22)),
        (isPlayer(player, board, 13, 14) or isPlayer(player, board, 10, 12)),
        (isPlayer(player, board, 17, 18) or isPlayer(player, board, 19, 21)),
        (isPlayer(player, board, 1, 9) or isPlayer(player, board, 16, 18)),
        (isPlayer(player, board, 16, 17) or isPlayer(player, board, 20, 23)),
        (isPlayer(player, board, 16, 21) or isPlayer(player, board, 3, 11)),
        (isPlayer(player, board, 12, 4) or isPlayer(player, board, 18, 23)),
        (isPlayer(player, board, 16, 19) or isPlayer(player, board, 22, 23)),
        (isPlayer(player, board, 6, 14) or isPlayer(player, board, 21, 23)),
        (isPlayer(player, board, 18, 20) or isPlayer(player, board, 21, 22))
    ]

    return mill[position]

def isMill(position, board):
    p = board[position]
    if p != 'x':
        return checkNextMill(position, board, p)
    else:
        return False

def numOfPieces(board, value):
    return board.count(value)

def removePiece(board_copy, board_list, player):
    for i in range(len(board_copy)):
        if player == '1':
            opp = '2'
        else:
            opp = '1'
        if(board_copy[i] == opp):
            if not isMill(i, board_copy):
                new_board = deepcopy(board_copy)
                new_board[i] = 'x'
                # Making a new board and emptying the position where piece is removed
                board_list.append(new_board)
    return board_list

def possibleMoves_stage1(board):
    board_list = []
    for i in range(len(board)):
        # Fill empty positions with player 1
        if(board[i] == 'x'):
            # Creating a clone of the current board
            # and removing pieces if a Mill can be formed
            board_copy = deepcopy(board)
            board_copy[i] = '1'

            if (isMill(i, board_copy)):
                # Remove a piece if a mill is formed on that position
                board_list = removePiece(board_copy, board_list, '1')
            else:
                # No mill, so just append the position
                board_list.append(board_copy)

    return board_list

def possibleMoves_stage2(board, player):

    board_list = []
    for i in range(len(board)):
        if(board[i] == player):
            adjacent_list = adjacentLocations(i)

            for pos in adjacent_list:
                if (board[pos] == 'x'):
                    # If the location is empty, then the piece can move there
                    # Hence, generating all possible combinations
                    board_copy = deepcopy(board)
                    board_copy[i] = 'x'
                    # Emptying the current location, moving the piece to new position
                    board_copy[pos] = player

                    if isMill(pos, board_copy):
                        # in case of mill, remove Piece
                        board_list = removePiece(
                            board_copy, board_list, player)
                    else:
                        board_list.append(board_copy)
    return board_list


# Generating all possible moves for stage 3 of the game
# That is, when one player has only 3 pieces
def possibleMoves_stage3(board, player):

    board_list = []

    for i in range(len(board)):
        if(board[i] == player):
            for j in range(len(board)):
                if (board[j] == 'x'):
                    board_copy = deepcopy(board)
                    # The piece can fly to any empty position, not only adjacent ones
                    # So, generating all possible positions for the pieces
                    board_copy[i] = 'x'
                    board_copy[j] = player

                    if isMill(j, board_copy):
                        # If a Mill is formed, remove piece
                        board_list = removePiece(
                            board_copy, board_list, player)
                    else:
                        board_list.append(board_copy)
    return board_list


# Checks if game is in stage 2 or 3
# Returns possible moves accordingly
def possibleMoves_stage2or3(board, player='1'):
    if numOfPieces(board, player) == 3:
        return possibleMoves_stage3(board, player)
    else:
        return possibleMoves_stage2(board, player)
