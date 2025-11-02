import time
from utils import draw_grid
import heapq


def dijkstra(start, end, grid, canvas):
    """Dijkstra's algorithm visualization using a priority queue.

    Treats each edge with cost 1. Skips non-walkable neighbors.
    """
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    distance = {start: 0}

    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            reconstruct_path(came_from, current, grid, canvas)
            return

        for neighbor in get_neighbors(current, grid):
            if not getattr(neighbor, "walkable", True):
                continue

            tentative_distance = distance[current] + 1

            if neighbor not in distance or tentative_distance < distance[neighbor]:
                distance[neighbor] = tentative_distance
                came_from[neighbor] = current
                heapq.heappush(open_set, (distance[neighbor], neighbor))

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

