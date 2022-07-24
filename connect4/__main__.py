from connect4 import Board
from connect4.connect4 import Piece


if __name__ == "__main__":
    board = Board()
    turn = Piece.BLACK
    while (winner := board.get_winner()) is None:
        try:
            print(str(board))
            print("".join(str(i) for i in range(len(str(board).splitlines()[0]))))
            move = int(input(f"{turn.name}'s turn: "))
            board.add_piece(turn, move)
            turn = next(turn)
        except Exception as e:
            print(f"Invalid move: {type(e)}: {e}")
    print(f"{winner.name} wins!")
