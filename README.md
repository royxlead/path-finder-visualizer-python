# Path Finder Visualizer (Python – Tkinter)

An interactive **pathfinding algorithm visualizer** built with **Python** and **Tkinter**. Easily visualize how BFS, DFS, A\*, and Dijkstra's algorithms traverse a grid to find the shortest path.

## Features

* **Algorithm Visualizations**: Supports:

  * BFS (Breadth-First Search)
  * DFS (Depth-First Search)
  * A\* (A-Star)
  * Dijkstra's Algorithm
* **Interactive Grid UI**: Click to set customized **start (blue)** and **end (orange)** nodes, then watch pathfinding unfold.
* **Grid Auto-Reset**: After each run, the grid resets automatically for a fresh visualization. ([GitHub][1])

## Installation & Running

1. **Clone the repository**

   ```bash
   git clone https://github.com/royxlead/path-finder-visualizer-python.git
   cd path-finder-visualizer-python
   ```

2. **Install dependencies**
   Ensure you have **Python 3.7+** installed.
   (Currently no external dependencies specified; modify as needed.) ([GitHub][1])

3. **Run the application**

   ```bash
   python main.py
   ```

## Usage Guide

1. Launch opens an interactive grid window.
2. Set **start node** (blue) and **end node** (orange) via clicks.
3. Choose a pathfinding algorithm from available options.
4. Run the visualization and observe the pathfinding in real time.
5. After completion, the grid resets automatically for your next try. ([GitHub][1])

## Code Structure

```
path-finder-visualizer-python/
├── main.py          # GUI controller and application entry point
├── algorithms/      # Implementations of BFS, DFS, A*, Dijkstra's
├── node.py          # Definition and behavior of individual grid nodes
├── helper.py        # Support functions for grid interactions
├── utils.py         # Helper utilities (e.g., grid drawing, reset logic)
├── README.md        # This documentation
└── LICENSE          # MIT License file
```

([GitHub][1])

## Customization

* Modify grid behavior, node colors, or algorithm speed via parameters in `main.py` or `node.py`.
* Easily extend features like adjustable grid size or add maze generation. ([GitHub][1])

## Future Enhancements

* Support **manual obstacle placement** and **grid resizing**.
* Introduce **diagonal movement** and **weighted nodes** for complex visualization.
* Add **UI improvements**—like animation speed control or algorithm selection dropdowns.

## Contribution

Contributions are welcome! Feel free to fork, tweak, and submit a pull request.
