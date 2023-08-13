import itertools
import random
from typing import Iterable, Iterator
from pprint import pp
from PIL import Image, ImageDraw
from cell import Cell

from cell import Cell
from distances import Distances

Color = tuple[int, int, int]

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
        for cell in self:
            row, col = cell.row, cell.column

            cell.north = self[row - 1, col]
            cell.south = self[row + 1, col]
            cell.west = self[row, col - 1]
            cell.east = self[row, col + 1]

    def row_iter(self) -> Iterable[list[Cell]]:
        return iter(self.grid)
    
    def random_cell(self) -> Cell:
        row = random.randint(0, self.rows - 1)
        column = random.randint(0, self.columns - 1)
        return self.grid[row][column]
    
    def __getitem__(self, index: tuple[int, int]) -> Cell | None:
        row, column = index
        if row not in range(self.rows):
            return None
        if column not in range(self.columns):
            return None
        return self.grid[row][column]

    def __iter__(self) -> Iterator[Cell]:
        return itertools.chain.from_iterable(self.grid)
    
    def __len__(self) -> int:
        return self.rows * self.columns
    
    def __repr__(self) -> str:
        output = "+" + "---+" * self.columns + "\n"
        for row in self.row_iter():
            top = "|"
            bottom = "+"

            for cell in row:
                contents = self.contents_of(cell)
                body = f" {contents} " # Three spaces
                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body + east_boundary

                south_boundary = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner

            output += top + "\n"
            output += bottom + "\n"

        return output
    
    def contents_of(self, cell: Cell) -> str:
        return " "
    
    def background_color_of(self, cell: Cell) -> Color | None:
        return None
    
    def to_png(self, cell_size: int = 10) -> Image.Image:
        padding = 5
        img_width = cell_size * self.columns + padding*2
        img_height= cell_size * self.rows + padding*2

        background = (255, 255, 255)
        wall = (0, 0, 0)

        image = Image.new('RGBA', (img_width+1, img_height+1), color=background)
        draw = ImageDraw.Draw(image)
        
        for mode in ['backgrounds', 'walls']:
            for cell in self:
                x1 = cell.column * cell_size + padding
                y1 = cell.row * cell_size + padding
                x2 = (cell.column + 1) * cell_size + padding
                y2 = (cell.row + 1) * cell_size + padding

                if mode == 'backgrounds':
                    color = self.background_color_of(cell)
                    draw.rectangle((x1, y1, x2, y2), fill=color)
                else:
                    if cell.north is None:
                        draw.line((x1, y1, x2, y1), wall)
                    if cell.west is None:
                        draw.line((x1, y1, x1, y2), wall)
                    if not cell.is_linked(cell.east):
                        draw.line((x2, y1, x2, y2), wall)
                    if not cell.is_linked(cell.south):
                        draw.line((x1, y2, x2, y2), wall)

        return image
    
class DistanceGrid(Grid):
    def __init__(self, rows: int, columns: int) -> None:
        super().__init__(rows, columns)
        self.distances : Distances | None = None

    def contents_of(self, cell: Cell) -> str:
        try:
            distances = self.distances
            if distances:
                distance = distances[cell]
                return self.to_base36(distance)
        except KeyError:
            pass
            
        return super().contents_of(cell)
    
    def to_base36(self, i: int) -> str:
        BASE_36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if i < len(BASE_36):
            return BASE_36[i]
        else:
            return '!'

class ColoredGrid(Grid):
    def __init__(self, rows: int, columns: int) -> None:
        super().__init__(rows, columns)
        self._distances: Distances | None = None
        self._maximum: int | None = None

    @property
    def distances(self) -> Distances | None:
        return self._distances
    
    @distances.setter
    def distances(self, distances: Distances) -> None:
        self._distances = distances
        _, max_distance = distances.max()
        self._maximum = max_distance

    def background_color_of(self, cell: Cell) -> Color | None:
        if self._distances is None: return None
        if self._maximum is None: return None
        distance = self._distances[cell]
        if distance is None: return None

        intensity = float(self._maximum - distance) / self._maximum
        dark = round(255 * intensity)
        bright = 128 + round(127 * intensity)
        return (dark, bright, bright)
    
