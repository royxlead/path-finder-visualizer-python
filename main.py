import tkinter as tk
from tkinter import ttk
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.a_star import a_star
from algorithms.dijkstra import dijkstra
from node import Node, ROWS, COLS

window = tk.Tk()
window.title("Path Finder Visualizer")

canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

grid = []

def initialize_grid():
    global grid
    grid = [[Node(row, col) for col in range(COLS)] for row in range(ROWS)]
    
    start_node = grid[0][0]
    end_node = grid[ROWS - 1][COLS - 1]
    start_node.set_start()
    end_node.set_end()

    draw_grid()

def draw_grid():
    canvas.delete("all")  # Clear the canvas
    cell_width = canvas.winfo_width() // COLS
    cell_height = canvas.winfo_height() // ROWS

    for row in grid:
        for node in row:
            # node.x is row index, node.y is column index
            x1 = node.y * cell_width
            y1 = node.x * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height

            color = f"#{node.color[0]:02x}{node.color[1]:02x}{node.color[2]:02x}"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

def start_visualization(algorithm_name):
    initialize_grid()
    
    start = grid[0][0]
    end = grid[ROWS - 1][COLS - 1]
    
    auto_run_algorithm(algorithm_name, start, end)

def auto_run_algorithm(algorithm_name, start, end):
    if algorithm_name == "BFS":
        bfs(start, end, grid, canvas)
    elif algorithm_name == "DFS":
        dfs(start, end, grid, canvas)
    elif algorithm_name == "A*":
        a_star(start, end, grid, canvas)
    elif algorithm_name == "Dijkstra":
        dijkstra(start, end, grid, canvas)

selected_algorithm = tk.StringVar()
selected_algorithm.set("BFS")

algorithm_dropdown = ttk.Combobox(window, textvariable=selected_algorithm, values=["BFS", "DFS", "A*", "Dijkstra"])
algorithm_dropdown.pack()

start_button = tk.Button(window, text="Start Visualization", command=lambda: start_visualization(selected_algorithm.get()))
start_button.pack()

initialize_grid()

window.mainloop()
