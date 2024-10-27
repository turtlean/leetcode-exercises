class Solution:
    def snakesAndLadders(self, board) -> int:
        n = len(board)
        self.n = n
        self.board = board
        self.min_until_row_column = [[n**2 for c in range(n)] for r in range(n)]
        self.even_rows_towards_right = (self.n - 1) % 2 == 0
        return self.min_steps_from_row_column(self.n - 1, 0, 0)

    def min_steps_from_row_column(self, i, j, acum):
        if self.is_final_position(i, j):
            return acum
        if acum < self.min_until_row_column[i][j]:
            self.min_until_row_column[i][j] = acum

            tmp_min_steps = self.n**2
            for roll in range(1, 7):
                new_i, new_j = self.move_and_compute_next_position(i, j, roll)
                current_tmp_min_step = self.min_steps_from_row_column(
                    new_i, new_j, acum + 1
                )
                if current_tmp_min_step < tmp_min_steps:
                    tmp_min_steps = current_tmp_min_step
            return tmp_min_steps
        return self.n**2

    def move_and_compute_next_position(self, i, j, roll):
        row_offset = roll // self.n
        column_offset = roll % self.n

        new_i = i - row_offset

        if row_offset % 2 == 0:
            # Even difference makes j stay the same
            translated_j = j
        else:
            # Rotate j in a mirror fashion
            translated_j = self.n - 1 - j

        if self.even_rows_towards_right:
            if new_i % 2 == 0:
                if translated_j + column_offset > self.n - 1:
                    new_i = new_i - 1
                    new_j = translated_j + column_offset - (self.n - 1) - 1
                else:
                    new_j = translated_j + column_offset
            else:
                if translated_j - column_offset < 0:
                    new_i = new_i - 1
                    new_j = column_offset - translated_j - 1
                else:
                    new_j = translated_j - column_offset
        else:
            if new_i % 2 == 1:
                if translated_j + column_offset > self.n - 1:
                    new_i = new_i - 1
                    new_j = translated_j + column_offset - (self.n - 1) - 1
                else:
                    new_j = translated_j + column_offset
            else:
                if translated_j - column_offset < 0:
                    new_i = new_i - 1
                    new_j = column_offset - translated_j - 1
                else:
                    new_j = translated_j - column_offset

        if (0 <= new_i <= self.n - 1) and (0 <= new_j <= self.n - 1):
            if self.board[new_i][new_j] != -1:
                return self.compute_position_after_snake_lader(self.board[new_i][new_j])
        return new_i, new_j

    def compute_position_after_snake_lader(self, position):
        position = position - 1
        i = self.n - 1 - (position // self.n)
        if self.even_rows_towards_right:
            if i % 2 == 0:
                j = position % self.n
            else:
                j = (self.n - 1) - (position % self.n)
        else:
            if i % 2 == 1:
                j = position % self.n
            else:
                j = (self.n - 1) - (position % self.n)
        return i, j

    def is_final_position(self, i, j):
        if i < 0 or i == 0 and j <= 0:
            return True
        return False
