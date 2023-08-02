#!/usr/bin/env python

from grid import DistanceGrid
from binary_tree import BinaryTree
from distances import Distances

def main() -> int:
    grid = DistanceGrid(5, 5)
    BinaryTree.on(grid)

    start = grid[0, 0]
    if start is None:
        return 1

    distances = Distances.from_root(start)
    new_start, distance = distances.max()

    new_distances = Distances.from_root(new_start)
    goal, distance = new_distances.max()

    grid.distances = new_distances.path_to(goal)
    print(grid)

    return 0

if __name__ == '__main__':
    exit(main())
