import random
from typing import TypeVar, Sequence

from grid import Grid, ColoredGrid
from cell import Cell
from distances import Distances

T = TypeVar('T')

def sample(l: Sequence[T]) -> T:
    index = random.randint(0, len(l) - 1)
    return l[index]


class Wilsons:
    @classmethod
    def on(cls, grid: Grid) -> Grid:
        unvisited: list[Cell] = []
        for cell in grid:
            unvisited.append(cell)

        first = sample(unvisited)
        unvisited.remove(first)

        while unvisited:
            cell = sample(unvisited)
            path = [cell]

            while cell in unvisited:
                cell = sample(cell.neighbors())

                try:

                    position = path.index(cell)
                    path = path[0:position]
                except ValueError:
                    path.append(cell)
                    

            for index in range(0, len(path) - 1):
                path[index].link(path[index + 1])
                unvisited.remove(path[index])

        
        
        return grid

def main() -> int:
    grid = Grid(50, 50)
    Wilsons.on(grid)

    img = grid.to_png()
    img.save("maze_wilsons.png")

    for i in range(6):
        grid = ColoredGrid(50, 50)
        Wilsons.on(grid)

        start_row = round(grid.rows / 2)
        start_column = round(grid.columns / 2)
        start = grid[start_row, start_column]
        if start is None:
            return 1

        distances = Distances.from_root(start)
        grid.distances = distances
        
        img = grid.to_png()
        filename = f'maze_wilsons_{i:02d}.png'
        img.save(filename)

    return 0

if __name__ == "__main__":
    exit(main())
