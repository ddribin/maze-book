from cell import Cell
import itertools
from typing import Iterable
from pprint import pp

class Grid:
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self) -> list[list[Cell]]:
        grid = []
        for row in range(self.rows):
            r = []
            for column in range(self.columns):
                r.append(Cell(row, column))
            grid.append(r)
        return grid

    def configure_cells(self) -> None:
        for cell in self.cell_iter():
            row, col = cell.row, cell.column

            cell.north = self.get_cell(row - 1, col)
            cell.south = self.get_cell(row + 1, col)
            cell.west = self.get_cell(row, col - 1)
            cell.east = self.get_cell(row, col + 1)
    
    def get_cell(self, row: int, column: int) -> Cell | None:
        if row not in range(self.rows):
            return None
        if column not in range(self.columns):
            return None
        return self.grid[row][column]

    def row_iter(self) -> Iterable[list[Cell]]:
        return iter(self.grid)

    def cell_iter(self) -> Iterable[Cell]:
        return itertools.chain.from_iterable(self.grid)
    
    def count(self) -> int:
        return self.rows * self.columns
    
    def __str__(self) -> str:
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
