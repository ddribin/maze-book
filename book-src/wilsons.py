from grid import Grid, ColoredGrid
from cell import Cell
from distances import Distances
from utils import sample
import logging

class Wilsons:
    @classmethod
    def on(cls, grid: Grid) -> Grid:
        unvisited: list[Cell] = []
        for cell in grid:
            unvisited.append(cell)

        first = sample(unvisited)
        logging.debug(f'{first=}')
        unvisited.remove(first)

        while unvisited:
            logging.debug(f'{grid}')
            cell = sample(unvisited)
            path = [cell]
            logging.debug(f'{cell=}, {path=}')

            while cell in unvisited:
                cell = sample(cell.neighbors())
                logging.debug(f"{cell=}, {path=}")

                try:
                    position = path.index(cell)
                    path = path[0:position+1]
                except ValueError:
                    path.append(cell)
                    
            logging.debug(f'{path=}')
            for index in range(0, len(path) - 1):
                c1 = path[index]
                c2 = path[index+1]
                c1.link(c2)
                unvisited.remove(c1)
                logging.debug(f'{c1=} -> {c2=}')

        logging.debug(f'{grid}')
        return grid

def main() -> int:
    # logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    grid = Grid(20, 20)
    Wilsons.on(grid)

    img = grid.to_png()
    img.save("maze_wilsons.png")

    for i in range(6):
        grid = ColoredGrid(20, 20)
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
