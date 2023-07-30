from cell import Cell
import itertools
from typing import Iterable, Any
from pprint import pp
from PIL import Image, ImageDraw

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
    
    def to_png(self, cell_size: int = 10) -> Any:
        padding = 5
        img_width = cell_size * self.columns + padding*2
        img_height= cell_size * self.rows + padding*2

        background = (255, 255, 255)
        wall = (0, 0, 0)

        image = Image.new('RGBA', (img_width+1, img_height+1), color=background)
        draw = ImageDraw.Draw(image)
        
        for cell in self.cell_iter():
            x1 = cell.column * cell_size + padding
            y1 = cell.row * cell_size + padding
            x2 = (cell.column + 1) * cell_size + padding
            y2 = (cell.row + 1) * cell_size + padding

            if cell.north is None:
                draw.line((x1, y1, x2, y1), wall)
            if cell.west is None:
                draw.line((x1, y1, x1, y2), wall)
            if not cell.is_linked(cell.east):
                draw.line((x2, y1, x2, y2), wall)
            if not cell.is_linked(cell.south):
                draw.line((x1, y2, x2, y2), wall)

        return image
