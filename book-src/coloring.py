#!/usr/bin/env python

from grid import ColoredGrid
from binary_tree import BinaryTree
from distances import Distances

def main() -> int:
    grid = ColoredGrid(25, 25)
    BinaryTree.on(grid)

    start_row = round(grid.rows / 2)
    start_column = round(grid.columns / 2)
    start = grid[start_row, start_column]
    if start is None:
        return 1

    distances = Distances.from_root(start)
    grid.distances = distances
    img = grid.to_png()
    img.save("maze_colorized.png")

    return 0

if __name__ == '__main__':
    exit(main())
