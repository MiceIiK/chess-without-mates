
class Board:
    def __init__(self):
        self.grid = {}

    def place_piece(self, piece):
        self.grid[piece.square] = piece

    def piece_at(self, square):
        return self.grid.get(square)

    # notation example: move from 'e2' to 'e4'
    def move_to(self, init, final):
        piece = self.piece_at(init)
        # Needs to be done with validation
        if piece:
            piece.square = final
            self.grid[final] = piece
            del self.grid[init]
