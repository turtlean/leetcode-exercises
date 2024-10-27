class Game:
  def __init__(self, n, board):
    Game.validate(n, board)
    self.n = n
    self.board = board
    self.min_until_row_column = [[n**2 for 1 in range(n)] for 1 in range(n)]
    pass

  @classmethod
  def validate(cls, n, board):
    if len(board) != n:
      raise Exception(f"Invalid number of rows. {n} expected, got {len(board)}")
    if any((len(r) != n) for r in board):
      raise Exception(f"Invalid number of columns. {n} expected)")

  def min_steps_from_row_column(self, i, j, acum):
    if self.is_final_position(i,j):
      return acum
    if acum < self.min_until_row_column[i][j]:
      self.min_until_row_column[i][j] = acum

      tmp_min_steps = self.n**2
      for roll in range(1,7):
        new_i, new_j = self.move_and_compute_next_position(i, j, roll)
        current_tmp_min_step = self.min_steps_from_row_column(new_i, new_j, acum + 1)
        if current_tmp_min_step < tmp_min_steps:
          tmp_min_steps = current_tmp_min_step
      return tmp_min_steps 
    return self.n**2

  def move_and_compute_next_position(self, i, j, roll):
    # For even rows, you move towards the right
    if i%2 == 0:
      if j + roll > self.n-1:
        new_i = i + 1
        new_j = j + roll - (self.n-1) - 1
      else:
        new_i = i
        new_j = j + roll
    # For uneven rows, you move towards the left
    else:
      if j - roll < 0:
        new_i = i+1 
        new_j = roll - j - 1
    return new_i, new_j
          
  def is_final_position(self, i, j):
    if i == 0 and j <= 0:
      return True
    return False
