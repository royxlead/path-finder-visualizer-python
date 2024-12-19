from node import ROWS, COLS

def get_neighbors(node, grid):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in directions:
        new_row, new_col = node.row + d[0], node.col + d[1]
        if 0 <= new_row < ROWS and 0 <= new_col < COLS:
            neighbors.append(grid[new_row][new_col])
    return neighbors
