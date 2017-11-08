# Define blank list


def draw():
    board = []
    # Generate rows with length of 3
    for row in range(4):
        # Appen a blank list to each row cell
        board.append([])
        for column in range(4):
            # Assign x to each row
            board[row].append('x')
    return board


# Function will print board like an actual board
def print_board(board):
    for row in board:
        print " ".join(row)


board = draw()
print_board(board)
