from solution import Solution


def test_board_3x3():
    board = [[-1, 4, -1], [6, 2, 6], [-1, 3, -1]]
    assert Solution().snakesAndLadders(board) == 2
