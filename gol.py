from collections import defaultdict


class GOL:
    def __init__(self, rows, cols, cells, generation=1):
        self._rows = rows
        self._cols = cols
        self._generation = generation
        self._matrix = defaultdict(lambda: 0)
        for cell in cells:
            self._matrix[GOL.get_key(cell[0], cell[1])] = 1

    def round(self):
        new_matrix = defaultdict(lambda: 0)
        for i in range(self._rows):
            for j in range(self._cols):
                if self._live(i, j, self._compute_round(i, j)):
                    new_matrix[GOL.get_key(i, j)] = 1
        self._matrix = new_matrix
        self._generation += 1

    def _compute_round(self, i, j):
        total = 0
        for row in range(i-1, i+2):
            for col in range(j-1, j+2):
                if (row, col) != (i, j):
                    total += self._matrix[GOL.get_key(row, col)]
        return total

    def _live(self, i, j, neighbours):
        if self._matrix[GOL.get_key(i, j)] == 1:
            return 2 <= neighbours <= 3
        return neighbours == 3

    def serialize(self):
        return {
            'generation': self._generation,
            'row': self._rows,
            'col': self._cols,
            'cells': self._matrix.keys()
        }

    @staticmethod
    def get_key(row, col):
        return f'{row},{col}'
