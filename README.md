# Path Finder Visualizer

A **Path Finder Visualizer** built with Python and Tkinter to demonstrate popular pathfinding algorithms like BFS, DFS, A*, and Dijkstra. This interactive application allows users to visualize how different algorithms navigate from a start node to an end node on a grid.

## Features

- Visualize pathfinding algorithms:
  - **BFS (Breadth-First Search)**
  - **DFS (Depth-First Search)**
  - **A* Algorithm**
  - **Dijkstra's Algorithm**
- Interactive grid visualization.
- Customizable start and end nodes with distinct colors:
  - Start Node: **Blue**
  - End Node: **Orange**
- Automatically clears the grid after each run to allow fresh visualizations.

## Demo

[Insert screenshots or GIFs of the application in action.]

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/heysouravroy/Path-Finder-Visualizer.git
   cd Path-Finder-Visualizer
   ```

2. **Install Python dependencies**:
   Ensure you have Python 3.7+ installed.
   ```bash
   pip install -r requirements.txt
   ```
   *(Currently, this project does not have external dependencies, but use this step for future dependencies.)*

3. **Run the application**:
   ```bash
   python main.py
   ```

## Usage

1. Select a pathfinding algorithm from the dropdown menu.
2. Click the **Start Visualization** button.
3. Watch the selected algorithm explore the grid from the start node to the end node.
4. After completion, the grid will reset automatically for a new run.

## Code Structure

- **main.py**: Main application code that initializes the GUI and connects the algorithms.
- **algorithms/**: Contains individual Python files for each algorithm:
  - `bfs.py` - Implementation of Breadth-First Search.
  - `dfs.py` - Implementation of Depth-First Search.
  - `a_star.py` - Implementation of A* Algorithm.
  - `dijkstra.py` - Implementation of Dijkstra's Algorithm.
- **node.py**: Defines the `Node` class and grid structure.
- **utils.py**: Contains utility functions like drawing the grid.

## Customization

You can modify the `Node` colors, grid size, and visualization speed by editing the corresponding parameters in `node.py` and `main.py`.

## Future Enhancements

- Allow users to manually set start and end nodes.
- Add obstacles and weights to the grid.
- Add support for diagonal movement.
- Improve UI with better styling and animations.

## Contribution

Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

**Sourav Roy**  
GitHub: [heysouravroy](https://github.com/heysouravroy)  
LinkedIn: [heysouravroy](https://www.linkedin.com/in/heysouravroy/)
