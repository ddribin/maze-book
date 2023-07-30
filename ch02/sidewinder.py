from grid import Grid
from cell import Cell
import random

class Sidewinder:
    @classmethod
    def on(cls, grid: Grid) -> Grid:
        for row in grid.row_iter():
            run: list[Cell] = []

            for cell in row:
                run.append(cell)

                at_eastern_boundary = cell.east is None
                at_northern_boundery = cell.north is None

                should_close_out = (
                    at_eastern_boundary or
                    (not at_northern_boundery and (random.randint(0, 1) == 0))
                )

                if should_close_out:
                    index = random.randint(0, len(run)-1)
                    member = run[index]
                    if member.north:
                        member.link(member.north)
                    run.clear()
                else:
                    if cell.east:
                        cell.link(cell.east)
        return grid

if __name__ == "__main__":
    grid = Grid(4, 4)
    Sidewinder.on(grid)
    print(grid)
