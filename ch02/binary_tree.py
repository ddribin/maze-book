from grid import Grid
import random

class BinaryTree:
    @classmethod
    def on(cls, grid):
        for cell in grid.cell_iter():
            neighbors = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)

            index = random.randint(0, len(neighbors)-1)
            neighbor = neighbors[index]
            if neighbor != None:
                cell.link(neighbor)

        return grid
    

if __name__ == "__main__":
    grid = Grid(4, 4)
    BinaryTree.on(grid)
    print(grid)
