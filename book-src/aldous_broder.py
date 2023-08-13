from grid import Grid, ColoredGrid
from distances import Distances
from utils import sample

class AldousBroder:
    @classmethod
    def on(cls, grid: Grid) -> Grid:
        cell = grid.random_cell()
        unvisited = len(grid) - 1

        while unvisited > 0:
            neighbors = cell.neighbors()
            neighbor = sample(neighbors)

            if not neighbor.links():
                cell.link(neighbor)
                unvisited -= 1

            cell = neighbor

        return grid

def main() -> int:
    for i in range(6):
        grid = ColoredGrid(20, 20)
        AldousBroder.on(grid)

        start_row = round(grid.rows / 2)
        start_column = round(grid.columns / 2)
        start = grid[start_row, start_column]
        if start is None:
            return 1

        distances = Distances.from_root(start)
        grid.distances = distances
        
        img = grid.to_png()
        filename = f'maze_aldous_{i:02d}.png'
        img.save(filename)

    return 0

if __name__ == "__main__":
    exit(main())
