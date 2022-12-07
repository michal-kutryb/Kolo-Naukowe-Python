
def generate_board():
    board = []
    for i in range(0, 5):
        board.append(["*","*","*","*","*"])
    board[0][0] = "P"
    board[4][4] = "O"

    return board


def print_board(board):
    print("---------")
    for row in board:
        for x in row:
            print(x, end=' ')
        print()
    print("---------")
