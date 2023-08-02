from __future__ import annotations
from cell import Cell
from typing import Iterable

class Distances:
    def __init__(self, root: Cell) -> None:
        self.root = root
        self._cells = {root: 0}

    def __getitem__(self, item: Cell) -> int:
        return self._cells[item]
    
    def __contains__(self, item: Cell) -> bool:
        return item in self._cells
    
    def __setitem__(self, item: Cell, value: int) -> None:
        self._cells[item] = value

    def cells(self) -> list[Cell]:
        return list(self._cells.keys())
    
    def path_to(self, goal: Cell) -> Distances:
        current = goal
        
        breadcrumbs = Distances(self.root)
        breadcrumbs[current] = self._cells[current]

        while current != self.root:
            for neighbor in current.links():
                if self._cells[neighbor] < self._cells[current]:
                    breadcrumbs[neighbor] = self._cells[neighbor]
                    current = neighbor
                    break

        return breadcrumbs
    
    def max(self) -> tuple[Cell, int]:
        max_distance = 0
        max_cell = self.root

        for (cell, distance) in self._cells.items():
            if distance > max_distance:
                max_cell = cell
                max_distance = distance

        return (max_cell, max_distance)
    

    @staticmethod
    def from_root(root: Cell) -> Distances:
        distances = Distances(root)
        frontier = [root]

        while frontier:
            new_frontier: list[Cell] = []

            for cell in frontier:
                for linked in cell.links():
                    if linked in distances:
                        continue
                    distances[linked] = distances[cell] + 1
                    new_frontier.append(linked)

            frontier = new_frontier
        
        return distances
    

