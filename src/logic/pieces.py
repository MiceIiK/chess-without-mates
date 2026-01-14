from abc import ABC, abstractmethod


class Piece(ABC):
    # square is a list: [letter, num] where letter is a-h and num is 1-8
    def __init__(self, color, square):
        self.color = color
        self.square = square

    @abstractmethod
    def valid_moves(self, board):
        pass

    def __str__(self):
        return f"Color: {self.color} - AN: {self.__class__.__name__}"


class Pawn(Piece):
    def __init__(self, color, square):
        super().__init__(color, square)

    def valid_moves(self, board):
        potential_moves = []
        num = int(self.square[1]) + 1
        # Going right
        while (num <= 8):
            self.square = self.square[0] + str(num)
            if board.piece_at(self.square) is not None:
                break
            potential_moves.append(self.square)
            num += 1
        return potential_moves
