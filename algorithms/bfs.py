import time  
from utils import draw_grid
from node import Node

def bfs(start, end, grid, canvas):
    visited = set()
    queue = [start]
    came_from = {}

    while queue:
        current = queue.pop(0)

        if current == end:
            reconstruct_path(came_from, current, grid, canvas)
            return

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
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
