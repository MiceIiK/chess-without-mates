
def test_pawn_potential_moves():
    from src.logic.pieces import Pawn
    from src.logic.board import Board
    pawn = Pawn("white", "e2")
    obstacle = Pawn("black", "e7")
    board = Board()
    board.place_piece(pawn)
    board.place_piece(obstacle)
    moves = pawn.valid_moves(board)
    expected_moves = [
        "e3",
        "e4",
        "e5",
        "e6",
        "e7",  # posible capture
    ]
    assert moves == expected_moves
