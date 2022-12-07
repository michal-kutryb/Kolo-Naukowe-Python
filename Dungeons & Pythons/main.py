import board
from player import Player

ox = 4
oy = 4


def start_game():
    print("Dungeons & Pythons ver. 1.0")
    print("Your goal is to reach an apple")
    print("The player is shown on map as P, and an apple is shown as O")
    print("Type letter (wsad) to select direction for moving player")
    print("And confirm it by pressing ENTER button")
    print()


def get_input():
    print("Make your move: ")
    x = input().lower()
    print(x)
    if x != 'w' and x != 's' and x != 'a' and x != 'd':
        return 'err'
    return x


def game():
    start_game()
    p = Player(0, 0)
    game_board = board.generate_board()
    while p.px != ox or p.py != oy:
        board.print_board(game_board)
        move = 'err'
        while move == 'err':
            move = get_input()

        if move == "d" and p.py != 4:
            p.change_position(game_board, p.px, p.py+1)
        elif move == "s" and p.px != 4:
            p.change_position(game_board, p.px+1, p.py)
        elif move == "w" and p.px != 0:
            p.change_position(game_board, p.px-1, p.py)
        elif move == "a" and p.py != 0:
            p.change_position(game_board, p.px, p.py-1)

    board.print_board(game_board)
    print("You have reached the apple - You Won")


game()
