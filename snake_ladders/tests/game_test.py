from game import Game

def test_board_2x2():
  board = [[-1,-1],[-1,3]]
  g = Game(2, board)
  assert g.min_steps_from_row_column(1, 0, 0) == 1

def test_board_example():
  board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
  g = Game(6, board)
  assert g.min_steps_from_row_column(5, 0, 0) == 4

