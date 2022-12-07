class Player:

    def __init__(self, px, py):
        self.px = px
        self.py = py

    def change_position(self, board, ax, ay):
        board[self.px][self.py] = "*"
        self.px = ax
        self.py = ay
        board[self.px][self.py] = "P"

        return board
