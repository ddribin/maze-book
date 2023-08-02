from grid import Grid
from cell import Cell
import random
import sys
import os

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
    rows = 4
    columns = 4

    if len(sys.argv) >= 3:
        rows = int(sys.argv[1])
        columns = int(sys.argv[2])

    if len(sys.argv) == 4:
        seed = int(sys.argv[3])
    else:
        seed = int.from_bytes(os.urandom(8), 'big')
    random.seed(seed)

    grid = Grid(rows, columns)
    Sidewinder.on(grid)
    print(grid)
    print(f'Seed; {seed}')
    img = grid.to_png()
    img.save('maze.png')
