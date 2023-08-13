from grid import Grid, ColoredGrid
from cell import Cell
from utils import sample

class HuntAndKill:
    @classmethod
    def on(cls, grid: Grid) -> Grid:
        current: Cell | None = grid.random_cell()

        while current:
            unvisited_neighbors = [n for n in current.neighbors()
                                   if not n.links()]

            if unvisited_neighbors:
                random_neighbor = sample(unvisited_neighbors)
                current.link(random_neighbor)
                current = random_neighbor
            else:
                current = None

                for cell in grid:
                    visited_neighbors = [n for n in cell.neighbors()
                                         if n.links()]
                    cell_visited = bool(cell.links())
                    if not cell_visited and visited_neighbors:
                        current = cell
                        random_neighbor = sample(visited_neighbors)
                        current.link(random_neighbor)
                        break

        return grid

def main() -> int:
    grid = Grid(20, 20)
    HuntAndKill.on(grid)

    img = grid.to_png()
    img.save("maze_hunt_and_kill.png")

    return 0

if __name__ == "__main__":
    exit(main())
