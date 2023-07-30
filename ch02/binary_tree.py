from grid import Grid
from cell import Cell
import random
import sys

class BinaryTree:
    @classmethod
    def on(cls, grid: Grid) -> Grid:
        for cell in grid.cell_iter():
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
    if len(sys.argv) == 3:
        rows = int(sys.argv[1])
        columns = int(sys.argv[2])
    grid = Grid(rows, columns)
    BinaryTree.on(grid)
    print(grid)
