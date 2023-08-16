from grid import Grid
from cell import Cell
from utils import sample

class RecursiveBacktracker:
    @classmethod
    def on(cls, grid: Grid) -> Grid:
        start_at = grid.random_cell()
        stack = [start_at]

        while stack:
            current = stack[-1]
            neighbors = [n for n in current.neighbors() if not n.links()]

            if not neighbors:
                stack.pop()
            else:
                neighbor = sample(neighbors)
                current.link(neighbor)
                stack.append(neighbor)

        return grid

def main() -> int:
    grid = Grid(20, 20)
    RecursiveBacktracker.on(grid)

    img = grid.to_png()
    img.save("maze_recursive_backgracker.png")

    return 0
    return 0

if __name__ == "__main__":
    exit(main())
