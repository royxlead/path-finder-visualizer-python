import time  
from utils import draw_grid
from node import Node
import heapq

def a_star(start, end, grid, canvas):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            reconstruct_path(came_from, current, grid, canvas)
            return

        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
                came_from[neighbor] = current
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

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

def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def get_neighbors(node, grid):
    neighbors = []
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        neighbor_x = node.x + direction[0]
        neighbor_y = node.y + direction[1]
        
        if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]):
            neighbors.append(grid[neighbor_x][neighbor_y])
    
    return neighbors
