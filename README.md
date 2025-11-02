# Path Finder Visualizer (Python – Tkinter)

An interactive pathfinding algorithm visualizer built with Python and Tkinter. Use it to see how BFS, DFS, A*, and Dijkstra traverse a grid to find a path.

This repository is a small learning project and demo. It's intentionally lightweight and depends only on the Python standard library (Tkinter for UI).

## Highlights

- Visualizations for BFS, DFS, A*, and Dijkstra
- Simple Tkinter-based grid UI
- Clear code structure to learn from and extend

## Requirements

- Python 3.7 or newer
- Tkinter (usually included with standard Python distributions)

On most systems Tkinter is bundled with Python. If `tkinter` is missing, install it via your OS package manager (e.g., `apt`, `brew`, or Windows installer).

## Quick start (Windows / PowerShell)

Create and activate a virtual environment, then run the app:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python main.py
```

Or simply run with your system Python:

```powershell
python main.py
```

## Usage

1. The app opens a grid window. The default start node is blue (top-left) and the end node is orange (bottom-right).
2. Choose an algorithm from the dropdown (BFS, DFS, A*, Dijkstra).
3. Click "Start Visualization" to run the visualization.

Notes:
- The grid size and colors can be adjusted in `node.py` and `main.py`.
- The project currently uses automatic start/end placement; adding mouse-based placement and obstacle drawing is an easy extension.

## Development

- Code lives in these files:

```
main.py               # App entry and GUI
node.py               # Node data structure and helpers
utils.py              # Drawing helpers
helper.py             # Grid neighbor utilities
algorithms/           # BFS/DFS/A*/Dijkstra implementations
```

- A `.gitignore` has been added to ignore venvs, caches, and IDE files.

## Tests and linting (suggested next steps)

- Add a `requirements.txt` or `pyproject.toml` if you add non-stdlib dependencies.
- Add unit tests under a `tests/` directory covering algorithm correctness and neighbor logic.
- Optionally enable `black` and `flake8` for consistent formatting and linting.

## Contributing

Contributions and improvements are welcome. If you add features (mouse interaction, obstacle drawing, adjustable speed), please include tests and update the README to document them.

## License

MIT
