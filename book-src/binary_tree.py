from grid import Grid
from cell import Cell
import random
import sys
import os

class BinaryTree:
    @classmethod
    def on(cls, grid: Grid) -> Grid:
        for cell in grid:
            neighbors: list[Cell] = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)

            neighbor: Cell | None = None
            if len(neighbors) > 0:
                index = random.randint(0, len(neighbors)-1)
                neighbor = neighbors[index]
            if neighbor is not None:
                cell.link(neighbor)

        return grid
    

if __name__ == "__main__":
    rows = 4
    columns = 4

    if len(sys.argv) >= 3:
        rows = int(sys.argv[1])
        columns = int(sys.argv[2])

    if len(sys.argv) == 4:
        seed = int(sys.argv[3])
    else:
        seed = int.from_bytes(os.urandom(8))
    random.seed(seed)

    grid = Grid(rows, columns)
    BinaryTree.on(grid)
    print(grid)
    img = grid.to_png()
    img.save('maze.png')
