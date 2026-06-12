class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    @property
    def row(self):
        return self._row
    @row.setter
    def row(self, new_row):
        if new_row < 0:
            raise ValueError("row not positive")
        if new_row > 7 or new_row < 0:
            raise ValueError("row not on board")
        self._row = new_row
    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, new_column):
        if new_column < 0:
            raise ValueError("column not positive")
        if new_column > 7 or new_column < 0:
            raise ValueError("column not on board")
        self._column = new_column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False