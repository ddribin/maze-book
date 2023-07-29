from cell import Cell
import itertools
from pprint import pp

class Grid:
    def __init__(self, rows, columns) -> None:
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        grid = []
        for row in range(self.rows):
            r = []
            for column in range(self.columns):
                r.append(Cell(row, column))
            grid.append(r)
        return grid

    def configure_cells(self):
        for cell in self.cell_iter():
            row, col = cell.row, cell.column

            cell.north = self.get_cell(row - 1, col)
            cell.south = self.get_cell(row + 1, col)
            cell.west = self.get_cell(row, col - 1)
            cell.east = self.get_cell(row, col + 1)
    
    def get_cell(self, row, column):
        try:
            cell = self.grid[row][column]
        except IndexError:
            cell = None
        return cell

    def row_iter(self):
        return iter(self.grid)

    def cell_iter(self):
        return itertools.chain.from_iterable(self.grid)
    
    def count(self):
        return self.rows * self.columns
    
    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"
        for row in self.row_iter():
            top = "|"
            bottom = "+"

            for cell in row:
                body = "   " # Three spaces
                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body + east_boundary

                south_boundary = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner

            output += top + "\n"
            output += bottom + "\n"

        return output
