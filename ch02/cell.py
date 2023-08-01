from __future__ import annotations
from typing import Iterable

class Cell:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
        self._links: dict[Cell, bool] = {}
        self.north: Cell | None = None
        self.south: Cell | None = None
        self.east: Cell | None = None
        self.west: Cell | None = None

    def link(self, cell: Cell, bidi: bool = True) -> None:
        self._links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell: Cell, bidi: bool = True):
        del self._links[cell]
        if bidi:
            cell.unlink(self, False)

    def links(self) -> Iterable[Cell]:
        return self._links.keys()
    
    def is_linked(self, cell: Cell | None) -> bool:
        return cell in self._links
    
    def neighbors(self) -> list[Cell]:
        list = []
        if self.north: list.append(self.north)
        if self.south: list.append(self.south)
        if self.east: list.append(self.east)
        if self.west: list.append(self.west)
        return list
    
    def __str__(self) -> str:
        return f'Cell[{self.row}, {self.column})'
