from solution import Solution


def test_board_3x3():
    obstacle_grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert Solution().uniquePathsWithObstacles(obstacle_grid) == 2


def test_board_2x2():
    obstacle_grid = [[0, 1], [0, 0]]
    assert Solution().uniquePathsWithObstacles(obstacle_grid) == 1
