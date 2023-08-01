#!/usr/bin/env python

from grid import DistanceGrid
from distances import Distances
from binary_tree import BinaryTree

def main() -> int:
    grid = DistanceGrid(5, 5)
    BinaryTree.on(grid)

    start = grid[0, 0]
    if start is None:
        return 1
    
    distances = Distances.from_root(start)
    grid.distances = distances
    print(grid)
    return 0


if __name__ == '__main__':
    main()

