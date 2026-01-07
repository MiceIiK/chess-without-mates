from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, square):
        self.color = color
        self.square = square

    @abstractmethod
    def valid_moves(self, board):
        pass

    def __str__(self):
        return f"{self.color} {self.__class__.__name__}"
