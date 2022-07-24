from itertools import combinations
from unittest import TestCase

from connect4 import Board, Piece
from connect4.connect4 import Column


class PieceTestCase(TestCase):
    def test_uniqueness(self):
        for a, b in combinations(Piece, r=2):
            self.assertNotEqual(a, b)

    def test_piece_type_count(self):
        self.assertEqual(3, len(Piece))


class ColumnTestCase(TestCase):
    def test_empty_init(self):
        col = Column()
        for piece in col:
            self.assertEqual(Piece.EMPTY, piece)

    def test_add_piece_overflow(self):
        col = Column()
        for _ in range(6):
            col.add_piece(Piece.BLACK)
        try:
            col.add_piece(Piece.BLACK)
        except ValueError:
            pass


class BoardTestCase(TestCase):
    def test_columns_same_size(self):
        board = Board()
        for column in board:
            self.assertEqual(len(board[0]), len(column))

    def test_no_initial_winner(self):
        self.assertEqual(None, Board().get_winner())

    def test_vertical_win(self):
        board = Board()
        for _ in range(4):
            board.add_piece(Piece.RED, 0)
        self.assertEqual(Piece.RED, board.get_winner())

    def test_horizontal_win(self):
        board = Board()
        for i in range(4):
            board.add_piece(Piece.BLACK, i)
        self.assertEqual(Piece.BLACK, board.get_winner())

    def test_positive_diagonal_win(self):
        board = Board()
        for i in range(1, 4):
            for _ in range(i):
                board.add_piece(Piece.RED, i)
        for i in range(4):
            board.add_piece(Piece.BLACK, i)
        self.assertEqual(Piece.BLACK, board.get_winner())

    def test_negative_diagonal_win(self):
        board = Board()
        for i in range(1, 4):
            for _ in range(4 - i):
                board.add_piece(Piece.BLACK, i)
        for i in range(1, 5):
            board.add_piece(Piece.RED, i)
        self.assertEqual(Piece.RED, board.get_winner())
