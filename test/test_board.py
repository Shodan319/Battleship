from src.board import Board


def test_check_empty_board():
    board = Board()
    assert not board.check('A3')
