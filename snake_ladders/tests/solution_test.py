from solution import Solution


def test_board_3x3_second():
    board = [
        [-1, 17, -1, 6, -1, -1],
        [-1, 23, -1, 31, -1, -1],
        [-1, 35, -1, 28, -1, -1],
        [-1, 30, 24, -1, 13, -1],
        [-1, 10, -1, 16, 26, -1],
        [-1, -1, 27, 15, -1, -1],
    ]
    res = Solution().snakesAndLadders(board)
    assert res == 3


test_board_3x3_second()
