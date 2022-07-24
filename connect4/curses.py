from curses import (
    cbreak,
    COLOR_BLACK,
    color_pair,
    COLOR_RED,
    COLOR_YELLOW,
    curs_set,
    init_pair,
    noecho,
    wrapper,
)
from connect4 import Board, Piece


def init_screen(scr):
    scr.clear()
    curs_set(2)
    noecho()
    cbreak()
    init_pair(1, COLOR_YELLOW, COLOR_YELLOW)
    init_pair(2, COLOR_RED, COLOR_YELLOW)
    init_pair(3, COLOR_BLACK, COLOR_YELLOW)


def display_board(scr, board):
    for y, row in enumerate(str(board).splitlines()):
        scr.addstr(y, 0, row)
        for x, p in enumerate(row):
            match (p):
                case "E":
                    scr.chgat(y, x, 1, color_pair(1))
                case "R":
                    scr.chgat(y, x, 1, color_pair(2))
                case "B":
                    scr.chgat(y, x, 1, color_pair(3))


def display_winner(scr, winner):
    scr.addstr(7, 0, f"{winner} wins!")
    scr.getch()


def game_loop(scr):
    board = Board()
    turn = Piece.BLACK
    x, y = 0, 5
    while (winner := board.get_winner()) is None:
        display_board(scr, board)
        scr.move(y, x)
        key = scr.getkey()
        # Left: left arrow, a, j
        if key in ("KEY_LEFT", "a", "j"):
            x = 0 if x <= 0 else x - 1
        # Right: right arrow, d, ;
        if key in ("KEY_RIGHT", "d", ";"):
            x = 6 if x >= 6 else x + 1
        # Jump to column: 0-6
        if key in (str(n) for n in range(6)):
            x = int(key)
        # Place piece: enter, space
        if key in (" ", "\n"):
            board.add_piece(turn, x)
            turn = next(turn)
        for i, piece in enumerate(board[x]):
            if Piece.EMPTY == piece:
                y = len(board[x]) - i - 1
                break
    display_board(scr, board)
    display_winner(scr, winner)


def main(scr):
    init_screen(scr)
    game_loop(scr)


def play(options):
    wrapper(main)
