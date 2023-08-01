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
    

    @staticmethod
    def from_root(root: Cell) -> Distances:
        distances = Distances(root)
        frontier = [root]

        while frontier:
            new_frontier: list[Cell] = []

            for cell in frontier:
                for linked in cell.links():
                    print(f'  {linked}')
                    if linked in distances:
                        continue
                    distances[linked] = distances[cell] + 1
                    new_frontier.append(linked)

            frontier = new_frontier
        
        return distances
    

