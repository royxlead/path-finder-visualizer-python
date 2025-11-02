import time
from utils import draw_grid


def dfs(start, end, grid, canvas):
    """Depth-first search (iterative) visualization.

    Avoids revisiting nodes and skips non-walkable nodes.
    """
    visited = set()
    stack = [start]
    came_from = {}

    visited.add(start)

    while stack:
        current = stack.pop()

        if current == end:
            reconstruct_path(came_from, current, grid, canvas)
            return

        for neighbor in get_neighbors(current, grid):
            if not getattr(neighbor, "walkable", True):
                continue
            if neighbor in visited:
                continue

            visited.add(neighbor)
            stack.append(neighbor)
            came_from[neighbor] = current

            current.color = (255, 0, 0)
            draw_grid(grid, canvas)
            canvas.after(50)
            canvas.update()

    reconstruct_path(came_from, current, grid, canvas)

def reconstruct_path(came_from, current, grid, canvas):
    while current in came_from:
        current = came_from[current]
        current.color = (0, 255, 0) 
        draw_grid(grid, canvas)
        canvas.after(50)  
        canvas.update()

def get_neighbors(node, grid):
    neighbors = []
    x, y = node.x, node.y
    if x > 0:
        neighbors.append(grid[x - 1][y])
    if x < len(grid) - 1:
        neighbors.append(grid[x + 1][y])
    if y > 0:
        neighbors.append(grid[x][y - 1])
    if y < len(grid[0]) - 1:
        neighbors.append(grid[x][y + 1])

    return neighbors
