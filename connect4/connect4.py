from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional


class Piece(Enum):
    EMPTY = auto()
    RED = auto()
    BLACK = auto()

    def __str__(self):
        return self.name[0]

    def __repr__(self):
        return self.name

    def __next__(self):
        return Piece.BLACK if Piece.RED == self else Piece.RED


@dataclass
class Column:
    pieces: list[Piece] = field(init=False)

    def __post_init__(self):
        self.pieces = [Piece.EMPTY for _ in range(6)]

    def add_piece(self, piece: Piece):
        self.pieces[self.pieces.index(Piece.EMPTY)] = piece

    def __getitem__(self, index: int) -> Piece:
        return self.pieces[index]

    def __iter__(self):
        return iter(self.pieces)

    def __len__(self):
        return len(self.pieces)


@dataclass
class Board:
    columns: list[Column] = field(init=False)

    def __post_init__(self):
        self.columns = [Column() for _ in range(7)]

    def add_piece(self, piece: Piece, column: int):
        self[column].add_piece(piece)

    def get_winner(self) -> Optional[Piece]:
        # Check vertical
        for i in range(len(self)):
            for j in range(3, len(self[i])):
                if Piece.EMPTY != self[i][j] and all(
                    self[i][j] == self[i][j - k] for k in range(4)
                ):
                    return self[i][j]
        # Check horizontal
        for i in range(3, len(self)):
            for j in range(len(self[i])):
                if Piece.EMPTY != self[i][j] and all(
                    self[i][j] == self[i - k][j] for k in range(4)
                ):
                    return self[i][j]
        # Check positive diagonal
        for i in range(3, len(self)):
            for j in range(3, len(self[i])):
                if Piece.EMPTY != self[i][j] and all(
                    self[i][j] == self[i - k][j - k] for k in range(4)
                ):
                    return self[i][j]
        # Check negative diagonal
        for i in range(3, len(self)):
            for j in range(len(self[i]) - 3):
                if Piece.EMPTY != self[i][j] and all(
                    self[i][j] == self[i - k][j + k] for k in range(4)
                ):
                    return self[i][j]
        return None

    def __getitem__(self, index: int) -> Column:
        return self.columns[index]

    def __len__(self) -> int:
        return len(self.columns)

    def __str__(self):
        return "\n".join(
            "".join(str(p) for p in row)
            for row in [*zip(*self.columns, strict=True)][::-1]
        )
