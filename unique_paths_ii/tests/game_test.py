from game import Game


def test_board_3x7():
    g = Game(3, 7)
    assert g.unique_paths_from_position(1, 1) == 28

test_board_3x7()
