class InputProcessor:
    @staticmethod
    def process_input(filename):
        with open(filename) as f:
            lines = f.read().splitlines()
            assert len(lines) >= 3

            generation = InputProcessor._get_generation(lines[0])
            rows, cols = InputProcessor._get_rows_col(lines[1])

            assert len(lines) - 2 == rows

            cells = InputProcessor._get_cells(lines[2:], cols)

            return {
                'rows': rows,
                'cols': cols,
                'generation': generation,
                'cells': cells,
            }

    @staticmethod
    def _get_generation(line):
        generation = line.replace('Generation ', '').replace(':', '')
        assert generation.isdigit()
        return int(generation)

    @staticmethod
    def _get_rows_col(line):
        rows_cols = line.split(' ')
        assert len(rows_cols) == 2
        assert rows_cols[0].isdigit() and rows_cols[1].isdigit()
        return int(rows_cols[0]), int(rows_cols[1])

    @staticmethod
    def _get_cells(lines, cols):
        cells = []
        for row_index, row in enumerate(lines):
            assert len(row) == cols
            for col_index, cell in enumerate(row):
                if cell == '*':
                    cells.append((row_index, col_index))
        return cells
